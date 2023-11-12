## YOLOv8 Object Detection with Gradio

This repository contains an application built within the Gradio framework of the YOLOv8 object detection model. This app allows you to upload videos and view the uploaded video results in the right panel.

## Requirements
Before you begin, make sure the following required libraries are installed:

Python 3.6 or higher
pip package manager

## Installation

pip install gradio

## Before use

You can customize various parts of the app according to your requirements:

Model: change the line "model = YOLO("../output/weights/best.pt")" in app.py to the desired model file of YOLOv8 you have. Note the model directory when converting.

## Usage

1. Clone this repository to your computer:
    'https://github.com/cradle-uz/traffic_laws.git'
2. Go to the project branch: 'git checkout gradio-model-deployment'
3. Go to the project directory: 'cd gradio'
4. Run Gradio app: gradio python app.py via terminal or 'Run app.py' in PyCharm
5. Open your web browser and navigate to http://127.0.0.1:7860.
    ![image](https://github.com/cradle-uz/traffic_laws/assets/15974766/e68c4d70-dabc-40a0-84cc-49cb6853a5a5)
6. You will find the file upload button in the web interface. Click on it and select the video file you want to detect object.
    ![image](https://github.com/cradle-uz/traffic_laws/assets/15974766/b63c8744-23fd-42f3-bbad-af6ffc3d77cf)
7. After the video is uploaded, click "Submit" to start the process.
    ![image](https://github.com/cradle-uz/traffic_laws/assets/15974766/bfcceb5e-9f79-4d95-86c8-11ad2b002520)
8. After the video is loaded, the YOLOv8 model detects objects in the video frames. Detected objects are displayed in the right pane.
9. Important: Make sure that the process is running during the video process. The video process may take several minutes depending on the size of the uploaded video.
   
    ![image](https://github.com/cradle-uz/traffic_laws/assets/15974766/746900dd-d123-485c-8c2e-c9c31097790b)
10. After the completion of the video process, 2 new files should be created in the "Gradio" directory. The first is the output.mp4 file, which is a video consisting of frames that identify objects. The second is the annotated_frames.csv file, which contains the numbers of problematic frames and the times of each defined frame.
12. You can view the video result in video view in your web browser. Or open the output.mp4 with a video player.
