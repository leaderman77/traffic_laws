import glob
import gradio as gr
from gradio.components import Gallery, Video, Textbox
from classificatsion_video_demo import process

def predict(video_path):
    """
    Gradio interface orqali yuklab olingan videodan problem framelarni ajratib olinadi va resultat sifatida Galleryga chiqariladi
    :param video_path:
    :return:
    """
    # Your image processing code here
    print(video_path)
    problem, good, result = process(video_path)
    images = glob.glob(f'{result}/*.jpg')
    # selected_images = [images[0],images[len(images)//2],images[-1]]
    return problem+good, problem, good,images

my_example = [
    ['/home/asus/Downloads/Telegram Desktop/video/vid_39_1284-2_1202.mp4'],
    ['/home/asus/Downloads/Telegram Desktop/video/vid_39_1284-2_1204.mp4']
]

my_title = "Video Klassifikatsiya"
my_description = "128-4 qoida `To’xtash chizig’ini bosish` bo'yicha video analiz"
all_frame = Textbox(label="Umumiy framelar soni")
problem_frame = Textbox(label="Muammoli framelar soni")
good_frame = Textbox(label="Muammosiz framelar soni")

problem_frames = Gallery(label="Muammoli rasmlar", elem_id="gallery").style(
    grid=[3], height="auto"
)
input_video = Video(label="Kiruvchi video") # Create input video component

gr.Interface(fn=predict,
             inputs=input_video,
             outputs=[all_frame,problem_frame,good_frame,problem_frames],
             title=my_title,
             examples=my_example,
             description=my_description).launch(share=True)
