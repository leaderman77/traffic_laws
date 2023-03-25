import os
import pandas as pd


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
    values_xmin_list = list(info_dict["bbox_x"].values())       # xmin
    values_ymin_list = list(info_dict["bbox_y"].values())       # ymin
    values_xmax_list = list(info_dict["bbox_width"].values())   # xmax
    values_ymax_list = list(info_dict["bbox_height"].values())  # ymax
    values_iw_list = list(info_dict["image_width"].values())
    values_ih_list = list(info_dict["image_height"].values())

    # For each bounding box
    for i in range(len(values_xmin_list)):
        b_center_x = (values_xmin_list[i] + values_xmax_list[i]) / 2
        b_center_y = (values_ymin_list[i] + values_ymax_list[i]) / 2
        b_width = (values_xmax_list[i] - values_xmin_list[i])
        b_height = (values_ymax_list[i] - values_ymin_list[i])

        # Normalise the co-ordinates by the dimensions of the image
        b_center_x /= values_iw_list[i]
        b_center_y /= values_ih_list[i]
        b_width /= values_iw_list[i]
        b_height /= values_ih_list[i]
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
