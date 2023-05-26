import cv2
import os.path

import numpy as np
from ultralytics import YOLO
from file_utils import project_dir

path = "/home/kholbekov/Documents/Git/traffic_laws/scripts/vid_39_1284-2_1254.mp4"
saqlash_path = "vid_39_1284-2_1254"
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

s = 0
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
cap = cv2.VideoCapture(path)

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
            s += 1
        elif tekshirish(frame) == "Label natija: problem":
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame, 'problem', (0, 100), font, 2, (255, 255, 255), 3)
        # out.write(frame)
            cv2.imwrite(saqlash_path + "/%#05d.jpg" % s, frame)
            s += 1
        cv2.imshow('frame' ,frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()

out.release()

cv2.destroyAllWindows()