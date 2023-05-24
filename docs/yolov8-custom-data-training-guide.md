## Introduction
This document provides step-by-step instructions for preparing a custom dataset, training a YOLOv8 model on it, and running inference to check the predictions. By following these steps, you can customize and fine-tune the model for your specific use case, whether it is detecting traffic violations, recognizing objects in a particular setting, or anything else that requires object detection.

## Prerequisites
Before you start, make sure you have the following:

A computer with Python 3 installed
Ultralytics and other dependencies such as OpenCV, pandas, numpy installed
A GPU (optional, but recommended for faster training)
Annotated zip files containing your custom dataset (one file per video), stored in a local folder
A pre-trained YOLOv8 model (e.g., "yolov8n.pt") downloaded and saved in a folder

## Step 1: Preparing the custom dataset:
1. Ensure that you have all annotated zip files in a local folder, for example, zip_path=path/labels/cvat_label_results.
2. Create a **report** folder to save the results of the dataset creation to an Excel file.
3. Navigate to the `scripts/create_dataset.py` file and change **zip_path** to the path where you stored your zip files. 
   **report_file** to the path where you want to save the report Excel file.
4. Run `scripts/create_dataset.py` and check the results. This script creates **images** and **labels** folders, as well as a **file.csv** file.
5. Navigate to the `scripts/train_test_split.py` file. Change **images_path** and **labels_path** to the paths where you stored your images and labels in **step 4**.
6. Create a `dataset` folder and inside it create three subfolders named train, test, and val.
7. In the `scripts/train_test_split.py` file, change train_path, test_path, and val_path to the locations that you created in step 6, dataset/train, dataset/test, and dataset/val.
8. Check **test_size and val_size** values in the **split_data** function. The default values are 0.1 and 0.05 respectively. Change these values if necessary.
9. Run the script and check the result.

## Step 2: Training a YOLOv8 Model on Custom Dataset:
1. Create a folder named **output** in root of the project directory to save the results of training the model.
2. Create or change the existing **scripts/custom_data.yaml** file. This file specifies the path to the custom dataset. The class names for the training dataset.
3. Navigate to the `scripts/train_yolov8_traffic_laws.py` file. Set the model training parameters, such as **data**, **imgsz**, **epochs**, and **batch**. 
4. Make sure that you have a downloaded pretrained yolov8 model, for example, "yolov8n.pt". 
5. Change the **project** value in the model training and model validation statements, and set the output folder that you created in **step 1**.
6. Run the script and check the training progress.

## Step 3: Running Inference and Checking the Predictions:
1. For video sources, use `scripts/inference/video_inference.py` file. Change the **trained model path** (best.pt) and video_path. Run the file.
2. For image sources, use `scripts/inference/image_inference.py` file. Change the **trained model path** and image_path. Run the file
3. Inference results will be saved in the `scripts/inference/predict` folder. 
