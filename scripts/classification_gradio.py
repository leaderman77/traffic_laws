import os
import cv2
import numpy as np
import gradio as gr
import pandas as pd
from ultralytics import YOLO
from classificatsion_video_demo import process

def video_classiffication(video_path):
    print(video_path)
    return process(video_path)


# Define Gradio interface
iface = gr.Interface(video_classiffication, "video", "playable_video").launch()