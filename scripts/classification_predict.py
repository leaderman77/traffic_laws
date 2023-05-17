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
