import cv2
import os

def images_to_video(image_folder, video_name, fps):
    image_files = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort()

    frame = cv2.imread(os.path.join(image_folder, image_files[0]))
    height, width, layers = frame.shape

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_name, fourcc, fps, (width, height))

    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        frame = cv2.imread(image_path)
        video.write(frame)

    cv2.destroyAllWindows()
    video.release()

# Rasmlar papkasini va video nomini aniqlang
# image_folder = '/home/kholbekov/Documents/Git/traffic_laws/scripts/vid_39_1284-2_1293'
# video_name = 'vid_39_1284-2_1293_problem.mp4'
#
# # Kiritiladigan kadrlar sonini aniqlang
# fps = 24

# Rasmlarni video sifatida oqib olish funktsiyasini chaqirish
# images_to_video(image_folder, video_name = 'vid_39_1284-2_1293_problem.mp4', fps = 24)
