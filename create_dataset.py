import os
import pandas as pd
from utils import split_dataset


def extract_info_from_csv(csv_file):
    df = pd.read_csv(csv_file)
    # Convert the DataFrame to a dictionary
    dictionary = df.to_dict()
    # Print the resulting dictionary
    print(dictionary)
    return dictionary


def convert_to_yolov8(info_dict):
    print_buffer = []

    # Get the values of the dictionary as a list
    xmin_list = list(info_dict["bbox_x"].values())       # xmin
    ymin_list = list(info_dict["bbox_y"].values())       # ymin
    xmax_list = list(info_dict["bbox_width"].values())   # xmax
    ymax_list = list(info_dict["bbox_height"].values())  # ymax
    iw_list = list(info_dict["image_width"].values())
    ih_list = list(info_dict["image_height"].values())

    # For each bounding box
    for i in range(len(xmin_list)):
        xmax = xmax_list[i] + xmin_list[i]
        ymax = ymax_list[i] + ymin_list[i]
        b_center_x = (xmin_list[i] + xmax) / 2
        b_center_y = (ymin_list[i] + ymax) / 2
        b_width = (xmax - xmin_list[i])
        b_height = (ymax - ymin_list[i])

        # Normalise the co-ordinates by the dimensions of the image
        b_center_x /= iw_list[i]
        b_center_y /= ih_list[i]
        b_width /= iw_list[i]
        b_height /= ih_list[i]
        if b_height < 0:
            b_height = abs(b_height)

        # Write the bbox details to the file
        print_buffer.append(
            "{} {:.3f} {:.3f} {:.3f} {:.3f}".format(0, b_center_x, b_center_y, b_width, b_height))
    return print_buffer


def save_annotation_to_txt(info_dict, annot_list):
    values_img_names = list(info_dict["image_name"].values())
    for i in range(len(annot_list)):
        # Name of the file which we have to save
        save_file_name = os.path.join("data_label", "annotations", values_img_names[i].replace("jpg", "txt"))
        # Save the annotation to disk
        #print("\n".join(annot_list[i]), file=open(save_file_name, "w"))
        print(annot_list[i], file=open(save_file_name, "w"))


csv_file = 'data_label/data_label.csv'
info_dict = extract_info_from_csv(csv_file)
annot_list = convert_to_yolov8(info_dict)

save_annotation_to_txt(info_dict, annot_list)

split_dataset()
