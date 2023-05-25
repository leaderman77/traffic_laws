import os
import shutil
import random
from sklearn.model_selection import train_test_split
random.seed(5)



def split():
    """
    Bu funksiya datani YOLO formatga o'kazadi
    """
    # joy: good, problem fodlerlarini o'z ichigan oladi
    base_dir = 'traffic_laws/data/classification'  # folder containing:
    good_dir = os.path.join(base_dir, 'good')
    problem_dir = os.path.join(base_dir, 'problem')

    # saqlash uchun joylar
    output_dir = 'splitted'
    train_good_dir = os.path.join(output_dir, 'train/good')
    train_problem_dir = os.path.join(output_dir, 'train/problem')
    test_good_dir = os.path.join(output_dir, 'val/good')
    test_problem_dir = os.path.join(output_dir, 'val/problem')

    # Papkalarni yaratish agar ular mavjud bo'lmasa
    os.makedirs(train_good_dir, exist_ok=True)
    os.makedirs(train_problem_dir, exist_ok=True)
    os.makedirs(test_good_dir, exist_ok=True)
    os.makedirs(test_problem_dir, exist_ok=True)

    # hamm rasmlarning joyini olish
    good_images = os.listdir(good_dir)
    problem_images = os.listdir(problem_dir)

    # rasmlar ketma-ketligini o'zgartirish
    random.shuffle(good_images)
    random.shuffle(problem_images)

    # har bir good va problem ramslarini sanab, ulardan eng kichigi olish
    num_images = min(len(good_images), len(problem_images))

    # datani tenglashtirish
    good_images = good_images[:num_images]
    problem_images = problem_images[:num_images]

    # datani train va testga bo'lish
    good_train, good_test = train_test_split(good_images, test_size=0.05, random_state=42)
    problem_train, problem_test = train_test_split(problem_images, test_size=0.05, random_state=42)

    # tegishli papkalarga rasmlarni hoylashtirish
    for image in good_train:
        shutil.copy(os.path.join(good_dir, image), train_good_dir)

    for image in good_test:
        shutil.copy(os.path.join(good_dir, image), test_good_dir)

    for image in problem_train:
        shutil.copy(os.path.join(problem_dir, image), train_problem_dir)

    for image in problem_test:
        shutil.copy(os.path.join(problem_dir, image), test_problem_dir)
