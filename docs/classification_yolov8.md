## Classification Yolov8

#### The model receives an image, the model determines which class the image belongs to.

We have ``good/problem'' videos, the videos were captured using the following program.
(data videos [here](https://drive.google.com/drive/folders/1PK4pb5wXvD55c8zHqjyKvBpMStrQSAkV))

<details><summary>convert_from_video_to_image</summary>

```python
import os
import cv2


def convert_from_video_to_image(video_path):
     cam = cv2.VideoCapture(video_path)
     try:
         if not os.path.exists('data'):
             os.makedirs('data')
     except OSError:
         print('Error: Creating directory of data')
     # frame
     currentframe = 0
     while (True):
         # reading from frame
         ret, frame = cam.read()
         if ret:
             # if video is still left continue creating images
             name = './data/frame' + str(currentframe) + '.jpg'
             print('Creating...' + name)
             # writing the extracted images
             cv2.imwrite(name, frame)
             currentframe += 1
         otherwise:
             break
     cam.release()
     cv2.destroyAllWindows()
```

</details>

The `test/train' images were extracted using the following function.


<details><summary>train_test_split</summary>

```python
def train_test_split(source_directory, training_directory, testing_directory, split_size):
    """
    Assuming your source directory is 'my_images', and you want to split 80% for training and 20% for testing
    traffic_images
    │
    ├── good
    │   ├── img1.jpg
    │   ├── img2.jpg
    │   └── ...
    │
    └── problem
        ├── img1.jpg
        ├── img2.jpg
        └── ...
    Misol,
    source_directory = './traffic_images/'
    training_directory = './train/'
    testing_directory = './test/'
    train_test_split(source_directory, training_directory, testing_directory, split_size=0.8)
    """
    classes = ['good', 'problem']

    for cls in classes:
        os.makedirs(training_directory + cls, exist_ok=True)
        os.makedirs(testing_directory + cls, exist_ok=True)

        src_dir = os.path.join(source_directory, cls)
        files = os.listdir(src_dir)

        # randomize the files
        np.random.shuffle(files)

        # calculate the split index
        split_index = int(len(files) * split_size)

        # split the files
        train_files = files[:split_index]
        test_files = files[split_index:]

        # copy the split files into their respective directories
        for file in train_files:
            shutil.copy(os.path.join(src_dir, file), os.path.join(training_directory, cls, file))

        for file in test_files:
            shutil.copy(os.path.join(src_dir, file), os.path.join(testing_directory, cls, file))
```

</details>

#### Data tuzilishi quyidagicha

```commandline
good_problem_data
│
├── test
│   ├── img1.jpg
│   ├── img2.jpg
│   └── ...
│
└── train
    ├── img1.jpg
    ├── img2.jpg
    └── ...
```

Yuqorida `test/train` uchun rasmlarni ajratib datani tayyorlab oldik.

#### Train qilib ko'rganda `model = YOLO('yolov8n-cls.pt')` modulni yuklab olib, `data_path`ni modulga berib o'tamiz train qilish uchun. `model.train(data='/home/nuriddin/TrafficLaw/traffic_laws/data/good_problem_data', epochs=10, imgsz=64)`

<details><summary>train.py</summary>

```python
from ultralytics import YOLO


model = YOLO('yolov8n-cls.pt')  # load a pretrained model (recommended for training)

model.train(data='/home/nuriddin/TrafficLaw/traffic_laws/data/good_problem_data',
            epochs=10, imgsz=64)
```
</details>

<details><summary>train.py natijasi quyidagicha:</summary>

```doctest
  Epoch    GPU_mem       loss  Instances       Size
   1/10         0G     0.1393         10         64: 100%|██████████| 52/52 [00:20<00:00,  2.53it/s]
           classes   top1_acc   top5_acc: 100%|██████████| 7/7 [00:05<00:00,  1.39it/s]
               all       0.51          1

  Epoch    GPU_mem       loss  Instances       Size
   2/10         0G    0.04397         10         64: 100%|██████████| 52/52 [00:20<00:00,  2.53it/s]
           classes   top1_acc   top5_acc: 100%|██████████| 7/7 [00:04<00:00,  1.47it/s]
               all      0.995          1

  Epoch    GPU_mem       loss  Instances       Size
   3/10         0G    0.01353         10         64: 100%|██████████| 52/52 [00:19<00:00,  2.64it/s]
           classes   top1_acc   top5_acc: 100%|██████████| 7/7 [00:04<00:00,  1.48it/s]
               all      0.995          1

  Epoch    GPU_mem       loss  Instances       Size
   4/10         0G    0.01071         10         64: 100%|██████████| 52/52 [00:21<00:00,  2.45it/s]
           classes   top1_acc   top5_acc: 100%|██████████| 7/7 [00:04<00:00,  1.42it/s]
               all          1          1

  Epoch    GPU_mem       loss  Instances       Size
   5/10         0G    0.01882         10         64: 100%|██████████| 52/52 [00:20<00:00,  2.54it/s]
           classes   top1_acc   top5_acc: 100%|██████████| 7/7 [00:04<00:00,  1.42it/s]
               all      0.995          1

  Epoch    GPU_mem       loss  Instances       Size
   6/10         0G   0.001951         10         64: 100%|██████████| 52/52 [00:20<00:00,  2.56it/s]
           classes   top1_acc   top5_acc: 100%|██████████| 7/7 [00:04<00:00,  1.48it/s]
               all      0.995          1

  Epoch    GPU_mem       loss  Instances       Size
   7/10         0G   0.001908         10         64: 100%|██████████| 52/52 [00:20<00:00,  2.60it/s]
           classes   top1_acc   top5_acc: 100%|██████████| 7/7 [00:04<00:00,  1.50it/s]
               all          1          1

  Epoch    GPU_mem       loss  Instances       Size
   8/10         0G  0.0007607         10         64: 100%|██████████| 52/52 [00:19<00:00,  2.63it/s]
           classes   top1_acc   top5_acc: 100%|██████████| 7/7 [00:04<00:00,  1.49it/s]
               all          1          1

  Epoch    GPU_mem       loss  Instances       Size
   9/10         0G  0.0006301         10         64: 100%|██████████| 52/52 [00:19<00:00,  2.62it/s]
           classes   top1_acc   top5_acc: 100%|██████████| 7/7 [00:04<00:00,  1.50it/s]
               all          1          1

  Epoch    GPU_mem       loss  Instances       Size
  10/10         0G  0.0003573         10         64: 100%|██████████| 52/52 [00:20<00:00,  2.55it/s]
           classes   top1_acc   top5_acc: 100%|██████████| 7/7 [00:05<00:00,  1.37it/s]
               all          1          1
```
</details>


#### Train qilib bo'lgach, git orqali yuklangan `ultralytics` biblatekasi joylashgan faylda quyidagi ko'rsatilgan qismga borib train natijasini ko'rishimiz mumkin. <br>
`Logging results to /home/nuriddin/ultralytics/runs/classify/train1`

`train1`da quyidagi fayllarni mavjud. 

```doctest
train1
│
├── weights
    ├── best.pt
    ├── last.pt
```

`last.pt` orqali quyidagicha natijani `predict` qilishimiz mumkin.

<details><summary>predict.py</summary>

```python
from ultralytics import YOLO
import numpy as np


model = YOLO('/home/nuriddin/ultralytics/runs/classify/train13/weights/last.pt')


results = model('/home/nuriddin/TrafficLaw/traffic_laws/data/good_problem_data/test/good/frame4.jpg')

name = results[0].names # mavjud classlar
probs = results[0].probs.tolist() # yuz berish darajasi

print(name)
print(probs)

# yuz berish darajasi eng yuqori qiymatga ega classga tegishliligini ko'rish.
print(name[np.argmax(probs)])

```
</details>
