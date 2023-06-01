import glob
import gradio as gr
from gradio.components import Gallery, Video
from classificatsion_video_demo import process

def predict(video_path):
    # Your image processing code here
    print(video_path)
    result = process(video_path)
    images = glob.glob(f'{result}/*.jpg')
    return images

problem_frames = Gallery(label="Problem images", elem_id="gallery").style(
    grid=[4], height="auto"
)
input_video = Video(label="Input video") # Create input video component

gr.Interface(fn=predict, inputs=input_video, outputs=problem_frames).launch()