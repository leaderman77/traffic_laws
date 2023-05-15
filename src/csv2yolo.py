import os
import pandas as pd


# Define a function to convert the bounding box to YOLO format
def convert_to_yolo_format(label, width, height, x, y, w, h):
    yolo_x = (x + w / 2) / width
    yolo_y = (y + h / 2) / height
    yolo_w = w / width
    yolo_h = h / height
    return f"{label} {yolo_x} {yolo_y} {yolo_w} {yolo_h}"

# Define a dictionary to map label names to integer labels
label_map = {"yashil": 0, "qizil": 1, "sariq": 2, "stop-line": 3, "zebra-line":4, "cross-stop-line":5}


# Create the output directory if it doesn't exist
os.makedirs("yolo_labels_nuriddin", exist_ok=True)
# Parse the CSV content and convert it to the YOLO format
data = pd.read_csv("vid_39_1284-2_959.csv")

for idx, row in data.iterrows():
    image_name = row["image_name"].split(".")[0]  # Remove file extension
    yolo_filename = os.path.join("yolo_labels_nuriddin", f"{image_name}.txt")
    label = label_map[row["label_name"].strip()]
    image_width = int(row["image_width"])
    image_height = int(row["image_height"])
    bbox_x = int(row["bbox_x"])
    bbox_y = int(row["bbox_y"])
    bbox_width = int(row["bbox_width"])
    bbox_height = int(row["bbox_height"])

    yolo_line = convert_to_yolo_format(label, image_width, image_height, bbox_x, bbox_y, bbox_width, bbox_height)

    # Append the YOLO-formatted line to the corresponding label file
    with open(yolo_filename, "a") as yolo_file:
        yolo_file.write(yolo_line + "\n")
