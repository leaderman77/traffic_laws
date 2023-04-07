from ultralytics import YOLO

# model = YOLO('yolov8n.pt')
# model.predict(
#    output=r'C:\Users\sardo\Documents\DS\PyCharm\traffic_laws\data\train\images\frame0.jpg',
#    conf=0.25
# )

# Load a model
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)
# model = YOLO('yolov8n.yaml')  # build a new model from scratch
import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

# Use the model
results = model.train(data='data.yaml', epochs=1, batch=1, project=r"C:\Users\sardo\Documents\DS\PyCharm\cradle\traffic_laws\output")  # train the model

results = model.val(project=r"C:\Users\sardo\Documents\DS\PyCharm\cradle\traffic_laws\output")  # evaluate model performance on the validation set
#results = model('frame0.jpg')  # predict on an image
success = model.export(format='onnx')  # export the model to ONNX format