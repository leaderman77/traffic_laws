import os
from typing import Tuple, List
import cv2
from multiprocessing import Pool


def extract_frames(video_path: str, output_folder: str, filename: str) -> None:
    """
    Freymlarni videodan olish va rasm shaklda saqlash

    Parameters
    ----------
    video_path : str
        video fayl joyi
    output_folder : str
        rasm saqlanadigan joy
    filename : str
        video fayl nomi

    Examples
    --------
    >>> extract_frames("/video/joyi/video.mp4", "/rasm/joyi/output/", "video.mp4")
    """
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    while success:
        image = cv2.resize(image, (image.shape[1] // 2, image.shape[0] // 2))
        p = os.path.join(output_folder, f"frame_{count:06}_{filename.removesuffix('.mp4')}.jpg")
        if cv2.imwrite(p, image):
            print("saved:", p)
        else:
            print("Not saved")

        success, image = vidcap.read()
        count += 1


def prepare_tasks(root: str, save_path: str, folders: List[str]) -> List[Tuple[str, str, str]]:
    """
    Parallel videolarni protsess qilish uchun topshiriqlarni tayyorlaydi

    Parameters
    ----------
    root : str
        Videolar joyi
    save_path : str
        freym (rasm)lar saqlanadigan joy
    folders : List[str]
        Videolar joyi

    Returns
    -------
    tasks : List[Tuple[str, str, str]]
        topshiriqlar, har bir topshiriqda quyidagilar bo'ladi.
         [video_path, output_folder, and filename.

    Examples
    --------
    >>> prepare_tasks("/joy/root", "/joy/save", ["folder1", "folder2"])
    """
    tasks = []
    for folder in folders:
        for filename in os.listdir(os.path.join(root, folder)):
            if filename.endswith('.mp4'):
                tasks.append((os.path.join(root, folder, filename), f'{save_path}/' + folder, filename))
    return tasks


def process_videos(root: str, save_path: str, folders: List[str], pool_size: int) -> None:
    """
    Parallel ravishda hamma videolarni protsess qilish

    Parameters
    ----------
    root : str
        video joyi
    save_path : str
        Freymlar sqalanadigan joy
    folders : List[str]
        Videolarni saqlaydigan joy
    pool_size : int
        paralel ishlash o'lchami

    Examples
    --------
    >>> process_videos("/joy/root", "/joy/save", ["folder1", "folder2"], 4)
    """
    tasks = prepare_tasks(root, save_path, folders)
    with Pool(pool_size) as p:
        p.map(extract_frames, tasks)


root = 'traffic_laws/data/chiziqni-kesish/'
save_path = "traffic_laws/data/classification/"
folders = ['good', 'problem']

# Start the process
process_videos(root, save_path, folders, pool_size=16)
