import os
import cv2
import numpy as np
import gradio as gr
import pandas as pd
from ultralytics import YOLO

PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
model = YOLO(os.path.join(PROJECT_DIR, 'models', 'detection', 'best.pt'))

class_names = ['qizil', 'yashil', 'chiziq', 'keng_mashina_chiziqda']
colors = np.random.default_rng(3).uniform(0, 255, size=(len(class_names), 3))


def draw_detections(image, boxes, scores, cls_id, mask_alpha=0.3):
    """
    Kiritilgan rasmga bbox aniqlik darajasi va klass IDisini chizish funksiyasi

    Parameterlar:
    rasm (numpy.ndarray): detectionni chizish uchun berilgan rasm.
    boxes (List[numpy.ndarray]): [x1, y1, x2, y2] formatidagi bbox koordinatalari ro'yxati.
    scores (List[float]): Har bir detection uchun koifisent ballar.
    cls_id (int): Objekt idisi.
    mask_alpha (float): default 0.3ga teng

    Returns:
    numpy.ndarray: bbox detection chizilgan rasm.
    """
    mask_img = image.copy()
    det_img = image.copy()
    img_height, img_width = image.shape[:2]
    size = min([img_height, img_width]) * 0.0006
    text_thickness = int(min([img_height, img_width]) * 0.001)

    for box, score in zip(boxes, scores):
        color = colors[cls_id]
        x1, y1, x2, y2 = box.astype(int)
        cv2.rectangle(det_img, (x1, y1), (x2, y2), color, 2)
        cv2.rectangle(mask_img, (x1, y1), (x2, y2), color, -1)
        label = class_names[cls_id]
        caption = f'{label} {int(score * 100)}%'
        (tw, th), _ = cv2.getTextSize(text=caption, fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=size, thickness=text_thickness)
        th = int(th * 1.2)
        cv2.rectangle(det_img, (x1, y1), (x1 + tw, y1 - th), color, -1)
        cv2.rectangle(mask_img, (x1, y1), (x1 + tw, y1 - th), color, -1)
        cv2.putText(det_img, caption, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, size, (255, 255, 255), text_thickness, cv2.LINE_AA)
        cv2.putText(mask_img, caption, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, size, (255, 255, 255), text_thickness, cv2.LINE_AA)

    return cv2.addWeighted(mask_img, mask_alpha, det_img, 1 - mask_alpha, 0)


def detect_objects_on_video(video_path):
    """
    Video faylda ob'ektni aniqlashni ishga tushirish va aniniqlangan muamoli
    framelarni saqlash funksiyasi.
    Funksiya 2ta fayl yaratadi: Birinchisi, aniqlangan muammoli framelarni va
    ularni vaqtini csv shaklida faylga saqlidi. Ikkinchisi, aniqlangan muammoli
    framelar asosida video fayl

    Parameterlar:
    video_path (str): video fayl joylashgan joy.

    Returns:
    str: string korinishidagi video resultat.
    """
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'h264')
    out = cv2.VideoWriter('output.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS),
                          (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
    annotated_frames = []
    annotated_timestamps = []
    frame_number = 0

    while True:
        # Videodan framelarni o'qish
        ret, frame = cap.read()

        if not ret:
            break

        # detection resultatini olish
        results = model(frame, conf=0.1)

        # Tekshirish: agar "keng_mashina_chiziqda" labelli shu frameda bormi
        has_annotation = False
        label = None
        for i in range(len(results)):
            boxes = results[i].boxes
            # orginal rasm
            image = results[i].orig_img
            for j in range(len(boxes)):
                label = boxes[j].cls
                bbox_tensor = boxes[j].xyxy
                print(class_names[int(label)])

                # bbox kordinatalarini NumPy array [x1, y1, x2, y2] korinishda olish
                det_box = bbox_tensor[0].cpu().numpy()
                bbox_tensor_conf = boxes[j].conf
                conf = bbox_tensor_conf[0].cpu().numpy()
                frame = draw_detections(image, [det_box], [conf], int(label))

                # Tekshirish: Klass nomi "keng_mashina_chiziqda" ga tengmi
                if class_names[int(label)] == "keng_mashina_chiziqda":
                    has_annotation = True

        # Annotation bor framelarni raqamini chop etish
        if has_annotation:
            annotated_frames.append(frame_number)
            # muammoli framelarni videodagi vaqtini aniqlash va chop etish
            annotated_timestamps.append(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0)
            print("Frame", frame_number, "has the annotation")

            if label is not None and class_names[int(label)] == "keng_mashina_chiziqda":
                out.write(frame)

        frame_number += 1
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    df_annotated_frames = pd.DataFrame({'Frame Number': annotated_frames,
                                        'Timestamp (s)': annotated_timestamps})

    df_annotated_frames.to_csv('annotated_frames.csv', index=False)

    print("Annotated frames:")
    for frame_number, timestamp in zip(annotated_frames, annotated_timestamps):
        print("Frame", frame_number, "- Timestamp:", timestamp)

    # natija
    return "output.mp4"


# Gradio interfayini aniqlash
iface = gr.Interface(detect_objects_on_video, "video", "playable_video").launch()
