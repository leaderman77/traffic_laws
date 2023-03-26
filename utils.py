import os
import shutil
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
from sklearn.model_selection import train_test_split

class_id = 0


# Utility function to move images
def move_files_to_folder(list_of_files, destination_folder):
    for f in list_of_files:
        try:
            shutil.move(f, destination_folder)
        # except:
        #     print(f)
        #     assert False
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
