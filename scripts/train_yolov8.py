import os
from ultralytics import YOLO

PROJECT_DIR = os.path.dirname(os.path.dirname(__file__))

# load a pretrained model (recommended for training)
model = YOLO('yolov8n.pt')

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

out_path = os.path.join(PROJECT_DIR, 'output')
data_path = os.path.join(PROJECT_DIR, 'data', 'custom_data.yaml')

# train on the pretrained model
results = model.train(
    data=data_path,
    imgsz=640,
    epochs=2,
    batch=32,
    project=out_path,
    name='yolov8n_custom',
    save_period=2
)

# evaluate model performance on the validation set
results = model.val(project=out_path)