import os
import random
import cv2 as cv
from PIL import Image
import matplotlib.pyplot as plt
from utils import plot_bounding_box, plot_bounding_box_cv2

random.seed(0)

# set the path to the labels folder
labels_folder = "dataset/train/labels"

# choose a random annotation file from the list
annotation_file = random.choice(os.listdir(labels_folder))

# get the corresponding image file path
image_file = os.path.join(os.path.dirname(annotation_file), "dataset/train/images",
                          os.path.splitext(os.path.basename(annotation_file))[0] + ".jpg")
print(image_file)


def get_annotation_list():
    with open(os.path.join(labels_folder, annotation_file), "r") as file:
        annotation_list = file.read().split("\n")[:-1]
        annotation_list = [x.split(" ") for x in annotation_list]
        annotation_list = [[float(y) for y in x] for x in annotation_list]

    return annotation_list


def visualize_img_with_cv():
    annotation_list = get_annotation_list()
    # read the image file
    image = cv.imread(image_file)

    plot_bounding_box_cv2(image, annotation_list)

    # create a named window and set its properties
    cv.namedWindow("Image with Bounding Box", cv.WINDOW_NORMAL)
    cv.resizeWindow("Image with Bounding Box", (800, 500))

    # display the image with the bounding box
    cv.imshow("Image with Bounding Box", image)
    cv.waitKey(0)
    cv.destroyAllWindows()


def visualize_img_with_plt():
    annotation_list = get_annotation_list()

    # Load the image
    image = Image.open(image_file)

    # Plot the Bounding Box
    plot_bounding_box(image, annotation_list)


visualize_img_with_cv()
# visualize_img_with_plt()

