import cv2
import os

def visualize_yolo_annotations(image_dir, annotation_dir, ann):
    def convert_to_original_format(width, height, yolo_x, yolo_y, yolo_w, yolo_h):
        x = (yolo_x - yolo_w / 2) * width
        y = (yolo_y - yolo_h / 2) * height
        w = yolo_w * width
        h = yolo_h * height
        return int(x), int(y), int(w), int(h)

    # Define a dictionary to map integer labels to label names
    label_map = {0:"yashil", 1:"qizil", 2:"sariq", 3:"stop-line", 4:"zebra-line", 5:"cross-stop-line"}

    # Read the annotation file
    annotation_name = ann + ".txt"
    img_name = ann + ".png"
    annotation_path = os.path.join(annotation_dir, annotation_name)
    img_path = os.path.join(image_dir, img_name)
    image = cv2.imread(img_path)

    with open(annotation_path) as annotation_file:
        for line in annotation_file:
            label, yolo_x, yolo_y, yolo_w, yolo_h = map(float, line.strip().split())
            label_name = label_map[int(label)]

            # Convert YOLO-format bounding box to original format
            x, y, w, h = convert_to_original_format(image.shape[1], image.shape[0], yolo_x, yolo_y, yolo_w, yolo_h)

            # Draw the bounding box on the image
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, label_name, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the image with bounding boxes
    cv2.imshow("Annotated Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Usage example
image_dir = "resized_images"
annotation_dir = "yolo_labels_nuriddin"

anns = os.listdir(annotation_dir)
for ann in anns:
    visualize_yolo_annotations(image_dir, annotation_dir, ann.removesuffix(".txt"))
