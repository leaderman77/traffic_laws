import os
from ultralytics import YOLO

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

yolo_model = os.path.join(PROJECT_DIR, 'output/yolov8n_custom/weights/best.pt')
model = YOLO(yolo_model)

# save plotted images
plotted_result_path = os.path.join(PROJECT_DIR, 'scripts\inference')
image_path = os.path.join(PROJECT_DIR, 'data_for_inference\img')
results = model.predict(source=image_path, save=True, save_txt=True, show=True, project=plotted_result_path)