import os
import zipfile
import shutil
from tqdm import tqdm
import pandas as pd


def extract_zipfile(zip_path, tmp_folder):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(tmp_folder)


def copy_files(folder_path, new_folder_path, file_extension, name_prefix, counter):
    num_files = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.endswith(file_extension)])
    with tqdm(total=num_files) as pbar:
        for filename in os.listdir(folder_path):
            pbar.update(1)
            if filename.endswith(file_extension):
                # Generate a new filename for the file
                ext = os.path.splitext(filename)[1]
                new_filename = f"{name_prefix}_{counter:06d}{ext}"
                counter += 1

                # Copy the file to the new folder with the new name
                src_path = os.path.join(folder_path, filename)
                dst_path = os.path.join(new_folder_path, new_filename)
                shutil.copy(src_path, dst_path)
    return counter, num_files


def process_zipfiles(zip_path, images_path=None, labels_path=None):
    # Create the output folders if they don't exist
    os.makedirs(images_path, exist_ok=True)
    os.makedirs(labels_path, exist_ok=True)

    # Initialize counters for generating new filenames
    img_counter = 0
    label_counter = 0

    # Create an empty list to hold the statistical report data
    report_data = []

    # Iterate over each zip file in the specified directory
    for zip_file in os.listdir(zip_path):
        if zip_file.endswith(".zip"):
            print(f"Processing {zip_file}")
            # Extract the zip file to a temporary folder
            tmp_folder = "tmp_extracted"
            extract_zipfile(os.path.join(zip_path, zip_file), tmp_folder)

            # Initialize counters for the current zip file
            # num_images = 0
            # num_labels = 0

            try:
                # Copy image files to the images folder
                img_counter, num_images = copy_files(os.path.join(tmp_folder, "obj_train_data"), images_path, ".PNG", "frame", img_counter)

                # Copy label files to the labels folder
                label_counter, num_labels = copy_files(os.path.join(tmp_folder, "obj_train_data"), labels_path, ".txt", "frame", label_counter)


                # Clean up the temporary folder
                shutil.rmtree(tmp_folder)

                # Add the statistical report data for the current zip file to the report list
                report_data.append({"Zip File": zip_file,
                                    "Num Images": num_images,
                                    "Num Labels": num_labels})
            except:
                print(f"Error: {zip_file}")

    return report_data


def save_report(report_data, report_file):
    # Create a pandas DataFrame from the report data list
    report_df = pd.DataFrame(report_data)

    # Save the report DataFrame to an Excel file
    report_df.to_csv(report_file, index=False)
    print("Report file has been saved")


if __name__ == "__main__":
    # Set the paths for the zip files and output folders
    # zip_path = r"D:\DS\Projects\traffic_laws\targetlash\cvat_label_result"
    zip_path = "/home/cradle/work/git/traffic_laws/data/cvat_targetlangan"
    report_file = "/home/cradle/work/git/traffic_laws/report/file.csv"

    images_path = "/home/cradle/work/git/traffic_laws/data/yolo_format/images"
    labels_path = "/home/cradle/work/git/traffic_laws/data/yolo_format/labels"

    report_data = process_zipfiles(zip_path, images_path, labels_path)
    save_report(report_data, report_file)
