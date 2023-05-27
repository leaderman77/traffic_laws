## Berilgan videoni clasifikatsiya moduli orqali muammoli joylarni aniqlash

1. Videoni biz classifikatsiya modulidan foydalanib
    ```doctest
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
    ```
   kod orqali videoni fremnlarga o'tqazib, undagi muaamoli rasmlarni yuklab oldik va natijani va
   👉 [bu](https://drive.google.com/drive/folders/1TyijJpv5I1dOFQlUJkKayGSAhYv015n4) yerga yuklandi

2. olingan videolarni video ko'riinshiga
    ```doctest
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
    image_folder = '/home/kholbekov/Documents/Git/traffic_laws/scripts/vid_39_1284-2_1293'
    video_name = 'vid_39_1284-2_1293_problem.mp4'
    
    # Kiritiladigan kadrlar sonini aniqlang
    fps = 24
    
    # Rasmlarni video sifatida oqib olish funktsiyasini chaqirish
    images_to_video(image_folder, video_name, fps)
    
    ```
   codan foydalanib keltirdik va bu 👉 [bu](https://drive.google.com/drive/folders/1lPyXneWOwdVV4Qq-eP9mFpMcaoo-McxF)
   yerga yuklandi

## Xulosa:

| Nomi               | asli | problem | good |
|--------------------|------|---------|------|
| vid_39_1284-2_1174 | 117  | 1       | 116  |
| vid_39_1284-2_1202 | 38   | 18      | 20   |
| vid_39_1284-2_1204 | 76   | 24      | 52   |
| vid_39_1284-2_1207 | 50   | 22      | 28   |
| vid_39_1284-2_1215 | 93   | 68      | 25   |
| vid_39_1284-2_1220 | 104  | 7       | 97   |
| vid_39_1284-2_1237 | 39   | 30      | 9    |
| vid_39_1284-2_1250 | 52   | 20      | 32   |
| vid_39_1284-2_1254 | 67   | 47      | 20   |
| vid_39_1284-2_1293 | 386  | 358     | 28   |

Eng ko’p framelar soni `vid_39_1284-2_1293`da 386ta

Eng kam framelar soni `vid_39_1284-2_1202`da 38ta

Eng ko’p problem framelar `vid_39_1284-2_1293`da 358ta

Eng kam problem framelar `vid_39_1284-2_1174`da 1ta

Eng ko’p good framelar `vid_39_1284-2_1174`da 116ta

Eng kam good framelar `vid_39_1284-2_1237`da 9ta

Ba'zi xatoliklar ham aniqlandi ,videodagi problem qilib olingan lekin bular good uchunn misol boladi

`vid_39_1284-2_1202` 
![img.png](..%2Fdata%2Frasm%2Fimg.png)

`vid_39_1284-2_1220` 

![img_1.png](..%2Fdata%2Frasm%2Fimg_1.png)
![img_2.png](..%2Fdata%2Frasm%2Fimg_2.png)

Modul asosan qoida buzarlikdan oldinroq ya'ni aynan chiziq ustida emas undan oldinroq yoki keyinroqdan boshlamoqda