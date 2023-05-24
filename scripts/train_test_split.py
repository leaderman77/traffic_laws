import os
import shutil
from sklearn.model_selection import train_test_split
from tqdm import tqdm


def create_output_folders(train_path, test_path, val_path):
    os.makedirs(train_path, exist_ok=True)
    os.makedirs(test_path, exist_ok=True)
    os.makedirs(val_path, exist_ok=True)
    os.makedirs(os.path.join(train_path, "images"), exist_ok=True)
    os.makedirs(os.path.join(train_path, "labels"), exist_ok=True)
    os.makedirs(os.path.join(test_path, "images"), exist_ok=True)
    os.makedirs(os.path.join(test_path, "labels"), exist_ok=True)
    os.makedirs(os.path.join(val_path, "images"), exist_ok=True)
    os.makedirs(os.path.join(val_path, "labels"), exist_ok=True)


def copy_images_and_labels(src_path, dst_path, labels_path, folder_name, image_filenames):
    print(f"Copying {folder_name} images and labels...")
    for image_filename in tqdm(image_filenames):
        # Copy the image file to the folder
        src_img_path = os.path.join(src_path, image_filename)
        dst_img_path = os.path.join(dst_path, "images", image_filename)
        shutil.copy(src_img_path, dst_img_path)

        # Copy the corresponding label file to the folder with the same name
        label_filename = os.path.splitext(image_filename)[0] + ".txt"
        src_label_path = os.path.join(labels_path, label_filename)
        dst_label_path = os.path.join(dst_path, "labels", label_filename)
        shutil.copy(src_label_path, dst_label_path)


def split_data(images_path, labels_path, train_path, test_path, val_path, test_size=0.1, val_size=0.05, shuffle=True):
    # Set the paths for the train, test, and validation folders
    create_output_folders(train_path, test_path, val_path)

    # Get a list of all image filenames in the images folder
    image_filenames = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]

    # Split the image filenames into train, test, and validation sets
    train_image_filenames, test_image_filenames = train_test_split(image_filenames, test_size=test_size, shuffle=shuffle)
    train_image_filenames, val_image_filenames = train_test_split(train_image_filenames, test_size=val_size, shuffle=shuffle)

    # Copy train images and labels
    copy_images_and_labels(images_path, train_path, labels_path, "train", train_image_filenames)

    # Copy test images and labels
    copy_images_and_labels(images_path, test_path, labels_path, "test", test_image_filenames)

    # Copy validation images and labels
    copy_images_and_labels(images_path, val_path, labels_path, "validation", val_image_filenames)


if __name__ == "__main__":
    images_path = "/home/cradle/work/git/traffic_laws/data/yolo_format/images"
    labels_path = "/home/cradle/work/git/traffic_laws/data/yolo_format/labels"
    train_path = "/home/cradle/work/git/traffic_laws/data/yolo_format/dataset/train"
    test_path = "/home/cradle/work/git/traffic_laws/data/yolo_format/dataset/test"
    val_path = "/home/cradle/work/git/traffic_laws/data/yolo_format/dataset/val"

    split_data(images_path, labels_path, train_path, test_path, val_path)