import os
import cv2
import numpy as np
import gradio as gr
from gradio.components import Video
import pandas as pd
from ultralytics import YOLO
from classificatsion_video_demo import process

def video_classiffication(video_path):
    print(video_path)
    # result = process(video_path)
    # print(type(result),result)
    video_path = "vid_39_1284-2_1202_problem.mp4"
    return video_path



input_video = Video(label="Input video") # Create input video component
output_video = Video(label="Output video") # Create output video component
interface = gr.Interface(fn=video_classiffication, inputs=input_video, outputs=output_video, title="Video Processing") # Create interface
interface.launch() # Launch the interface
# Define Gradio interface
# iface = gr.Interface(video_classiffication, "video", "playable_video").launch()