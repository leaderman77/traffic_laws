import os.path

import numpy as np
from ultralytics import YOLO
from file_utils import project_dir

print(project_dir())
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


def tekshirish():
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
    test_rasm_joyi = os.path.join(
        project_dir(),
        "scripts",
        "splitted",
        "val",
        "good",
        "frame_000000_vid_39_1284-2_34good.jpg"
    )

    model_custom = YOLO(train_qilingan_model_joyi)
    natijalar = model_custom(test_rasm_joyi)  # predict on an image
    natija = natijalar[0].names[np.argmax(natijalar[0].probs.cpu().numpy())]

    print(f"Label natija: {natija}")

tekshirish()