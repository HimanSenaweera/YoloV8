#https://docs.ultralytics.com/tasks/classify/#models
from ultralytics import YOLO
import tensorflow as tf

model = YOLO(r"C:\Users\singer\Desktop\MachineLearning\OpenCV\YoloV8\Image_Classification\runs\classify\train2\weights\best.pt")  # load a custom model

# Predict with the model
results = model(r"C:\Users\singer\Desktop\MachineLearning\OpenCV\YoloV8\Image_Classification\dataset\val\rain\1690.jpg")  # predict on an image

#https://docs.ultralytics.com/modes/predict/#key-features-of-predict-mode

for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk#names: {0: 'lightning', 1: 'rain', 2: 'sandstorm', 3: 'snow'}