#https://docs.ultralytics.com/tasks/classify/#models
import streamlit as st
from ultralytics import YOLO
from io import BytesIO
from PIL import Image
import numpy as np

st.set_page_config(page_title="Yolo Image Classifier", page_icon="☃️🌧️🌩️", layout="centered")
class_names = ["lightning", "rain", "sandstorm" , "snow"]

hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}      /* Hide hamburger menu */
    header {visibility: hidden;}         /* Hide Streamlit header */
    footer {visibility: hidden;}         /* Hide Streamlit footer */
    .st-emotion-cache-12fmjuu {display: none;} /* Hide status bar */
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("""
<style>
/* page background */
[data-testid="stAppViewContainer"] {
  background-image: url("https://images.unsplash.com/photo-1562155618-e1a8bc2eb04f?q=80&w=1191&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
  background-size: cover;
  background-position: center;
}

</style>
""", unsafe_allow_html=True)


model = YOLO(r"C:\Users\singer\Desktop\MachineLearning\OpenCV\YoloV8\Image_Classification\runs\classify\train2\weights\best.pt")  # load a custom model

def read_file_as_image(data):
    img = Image.open(BytesIO(data))
    new_image = img.resize((400, 300))
    return new_image,np.array(img)

uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img,np_array=read_file_as_image(uploaded_file.read())

    results = model(np_array)  

    #https://docs.ultralytics.com/modes/predict/#key-features-of-predict-mode

    for result in results:
        boxes = result.boxes  # Boxes object for bounding box outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs  # Probs object for classification outputs
        obb = result.obb  # Oriented boxes object for OBB outputs
        result.save(filename="result.jpg")
        st.image(img)
        index=np.argmax(np.array(probs.data))
        prob=round(float((np.max(np.array(probs.data)))),2)
        st.success(f" There is a {prob} probabilty that this image is {class_names[index]} ")
        

else:
    st.info("Upload a image to get a prediction.")
