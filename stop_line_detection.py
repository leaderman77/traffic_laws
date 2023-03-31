from ultralytics import YOLO

# model = YOLO('yolov8n.pt')
# model.predict(
#    source=r'C:\Users\sardo\Documents\DS\PyCharm\traffic_laws\data\train\images\frame0.jpg',
#    conf=0.25
# )

# Load a model
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
# model = YOLO('yolov8n.yaml')  # build a new model from scratch
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

# Use the model
results = model.train(data='data.yaml', epochs=50, batch=8)  # train the model

results = model.val()  # evaluate model performance on the validation set
#results = model('frame0.jpg')  # predict on an image
success = model.export(format='onnx')  # export the model to ONNX format