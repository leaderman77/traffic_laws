import cv2
import os.path
from frame_do_video import images_to_video
import numpy as np
from ultralytics import YOLO
from file_utils import project_dir


def train():
    """
    Funksiya modelni train qiladi
    data uyidagi formatda bo'lish kerak
    # - splitted
    #     - train
    #         - good
    #         - problem
    #     - val
    #         - good
    #         - problem
    """

    data_joyi = 'traffic_laws/scripts/splitted/'
    model = YOLO('yolov8n-cls.pt')
    model.train(data=data_joyi, epochs=100, imgsz=224, batch=512, save_period=10, device='cuda:0', augment=True)
    metrics = model.val()
    print(metrics.top1)   # top1 aniqligi

def tekshirish(path2):
    """
    test qilish, model va rasmni berishimiz kerak
    """
    train_qilingan_model_joyi = os.path.join(
        project_dir(),
        "models",
        "classification",
        "tl-14",
        "weights/best.pt"
    )
    test_rasm_joyi =(path2)

    model_custom = YOLO(train_qilingan_model_joyi)
    natijalar = model_custom(test_rasm_joyi)  # predict on an image
    natija = natijalar[0].names[np.argmax(natijalar[0].probs.cpu().numpy())]
    return (f"Label natija: {natija}")



def process(video_path):

    saqlash_path = video_path.split('/')[-1].split(".")[0]
    problem_frame = 0
    good_frame = 0
    if not os.path.exists(saqlash_path):
        # Create a new directory because it does not exist
        os.makedirs(saqlash_path)
    cap = cv2.VideoCapture(video_path)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    # out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))
    out = cv2.VideoWriter(
            saqlash_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4)))
        )

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            frame = cv2.flip(frame,1)
            # print(tekshirish(frame))
            if tekshirish(frame) == "Label natija: good":
                font = cv2.FONT_HERSHEY_COMPLEX
                cv2.putText(frame, 'good', (0, 100), font, 2, (255, 255, 255), 3)
                good_frame += 1
            elif tekshirish(frame) == "Label natija: problem":
                font = cv2.FONT_HERSHEY_COMPLEX
                cv2.putText(frame, 'problem', (0, 100), font, 2, (255, 255, 255), 3)
            # out.write(frame)
                cv2.imwrite(saqlash_path + "/%#05d.jpg" % problem_frame, frame)
                problem_frame += 1
            # cv2.imshow('frame' ,frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()

    out.release()

    cv2.destroyAllWindows()

    # images_to_video(saqlash_path, video_name = saqlash_path+'_problem.mp4', fps = 24)

    return problem_frame,good_frame,saqlash_path
