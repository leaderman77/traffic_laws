import os
import shutil
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from sklearn.model_selection import train_test_split

class_id = 0
class_names = ['stop line']
rng = np.random.default_rng(3)
colors = rng.uniform(0, 255, size=(len(class_names), 3))


def project_dir():
    """
    Returns path to the project root
    Returns
    -------
    Path
        Return path to the project root
    """
    return os.path.dirname(os.path.dirname(__file__))


# Utility function to move images
def move_files_to_folder(list_of_files, destination_folder):
    for f in list_of_files:
        try:
            shutil.move(f, destination_folder)
        except Exception as e:
            print(f"Error moving file {f}: {e}")
            raise


def split_dataset():
    # Read images and annotations
    images = [os.path.join('data_img/images', x) for x in os.listdir('data_img/images')]
    annotations = [os.path.join('data_label/annotations', x) for x in os.listdir('data_label/annotations') if x[-3:] == "txt"]

    images.sort()
    annotations.sort()

    # Split the dataset into train-valid-test splits
    train_images, val_images, train_annotations, val_annotations = train_test_split(
        images, annotations, test_size=0.2, random_state=1)
    val_images, test_images, val_annotations, test_annotations = train_test_split(
        val_images, val_annotations, test_size=0.5, random_state=1)

    # Move the splits into their folders
    move_files_to_folder(train_images, 'dataset/train/images')
    move_files_to_folder(val_images, 'dataset/val/images')
    move_files_to_folder(test_images, 'dataset/test/images')
    move_files_to_folder(train_annotations, 'dataset/train/labels')
    move_files_to_folder(val_annotations, 'dataset/val/labels')
    move_files_to_folder(test_annotations, 'dataset/test/labels')


def plot_bounding_box_cv2(image, annotation_list):
    annotations = np.array(annotation_list)
    h, w, _ = image.shape
    for ann in annotations:
        obj_cls, center_x, center_y, width, height = ann
        x0 = int((center_x - width / 2) * w)
        y0 = int((center_y - height / 2) * h)
        x1 = int((center_x + width / 2) * w)
        y1 = int((center_y + height / 2) * h)

        print(ann)
        print(x0, y0, x1, y1)
        cv.rectangle(image, (x0, y0), (x1, y1), (0, 255, 0), 2)
        cv.putText(image, str(obj_cls), (x0, y0 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return image


def plot_bounding_box(image, annotation_list):
    annotations = np.array(annotation_list)
    w, h = image.size

    plotted_image = ImageDraw.Draw(image)

    transformed_annotations = np.copy(annotations)
    transformed_annotations[:, [1, 3]] = annotations[:, [1, 3]] * w
    transformed_annotations[:, [2, 4]] = annotations[:, [2, 4]] * h

    transformed_annotations[:, 1] = transformed_annotations[:, 1] - (transformed_annotations[:, 3] / 2)
    transformed_annotations[:, 2] = transformed_annotations[:, 2] - (transformed_annotations[:, 4] / 2)
    transformed_annotations[:, 3] = transformed_annotations[:, 1] + transformed_annotations[:, 3]
    transformed_annotations[:, 4] = transformed_annotations[:, 2] + transformed_annotations[:, 4]

    for ann in transformed_annotations:
        obj_cls, x0, y0, x1, y1 = ann
        plotted_image.rectangle(((x0, y0), (x1, y1)))
        print(obj_cls, x0, y0, x1, y1)
        plotted_image.text((x0, y0 - 10), [class_id])

    plt.imshow(np.array(image))
    plt.show()


def draw_detections(image, boxes, scores, class_ids, mask_alpha=0.3):
    mask_img = image.copy()
    det_img = image.copy()

    img_height, img_width = image.shape[:2]
    size = min([img_height, img_width]) * 0.0006
    text_thickness = int(min([img_height, img_width]) * 0.001)

    # Draw bounding boxes and labels of detections
    for box, score, class_id in zip(boxes, scores, class_ids):
        color = colors[class_id]

        x1, y1, x2, y2 = box.astype(int)

        # Draw rectangle
        cv.rectangle(det_img, (x1, y1), (x2, y2), color, 2)

        # Draw fill rectangle in mask image
        cv.rectangle(mask_img, (x1, y1), (x2, y2), color, -1)

        label = class_names[class_id]
        caption = f'{label} {int(score * 100)}%'
        (tw, th), _ = cv.getTextSize(text=caption, fontFace=cv.FONT_HERSHEY_SIMPLEX,
                                      fontScale=size, thickness=text_thickness)
        th = int(th * 1.2)

        cv.rectangle(det_img, (x1, y1),
                      (x1 + tw, y1 - th), color, -1)
        cv.rectangle(mask_img, (x1, y1),
                      (x1 + tw, y1 - th), color, -1)
        cv.putText(det_img, caption, (x1, y1),
                    cv.FONT_HERSHEY_SIMPLEX, size, (255, 255, 255), text_thickness, cv.LINE_AA)

        cv.putText(mask_img, caption, (x1, y1),
                    cv.FONT_HERSHEY_SIMPLEX, size, (255, 255, 255), text_thickness, cv.LINE_AA)

    return cv.addWeighted(mask_img, mask_alpha, det_img, 1 - mask_alpha, 0)
