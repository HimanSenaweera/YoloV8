# 🚗 Object Detection

This project is about a trained *Yolo11n* model for **vehicle number plate detection** and for this project I downloaded the dataset and annotated it manually.

Dataset Source: [Open Images Dataset – Vehicle Number Plates](https://storage.googleapis.com/openimages/web/visualizer/index.html?type=detection&set=train&c=%2Fm%2F01jfm_)

Annotation Tool: [Computer Vision Annotation Tool](https://www.cvat.ai/)

---
## 👁️ Demo

<table>
  <tr>
    <td style="text-align:center;">
      <img src="train_batch0.jpg" width="100%"/>
      <div><strong>traning</strong></div>
    </td>
    <td style="text-align:center;">
      <img src="val_batch0_pred.jpg" width="100%"/>
      <div><strong>Validation</strong></div>
    </td>
  </tr>
</table>
<table>
  <tr>
    <td style="text-align:center;">
      <img src="confusion_matrix_normalized.png" width="100%"/>
      <div><strong>Confusion matrix</strong></div>
    </td>
    <td style="text-align:center;">
      <img src="results.png" width="100%"/>
      <div><strong>losses</strong></div>
    </td>
  </tr>
</table>

---
# 🖼️ Image Classification (YOLO)

This project demonstrates *YOLO11n-CLS* trained for an **image classification task**.  
The task involves classifying images into four categories ( `lightning`, `rain`, `sandstorm`, `snow`).  

Dataset Source: [Open Images Dataset – Vehicle Number Plates](https://www.kaggle.com/datasets/jehanbhathena/weather-dataset)
---

## 👁️ Demo

<table>
  <tr>
    <td style="text-align:center;">
      <img src="train_batch1.jpg" width="100%"/>
      <div><strong>Training Samples</strong></div>
    </td>
    <td style="text-align:center;">
      <img src="val_classification.jpg" width="100%"/>
      <div><strong>Validation Predictions</strong></div>
    </td>
  </tr>
</table>

<table>
  <tr>
    <td style="text-align:center;">
      <img src="confusion_matrix_classification.png" width="100%"/>
      <div><strong>Confusion Matrix</strong></div>
    </td>
    <td style="text-align:center;">
      <img src="results_classification.png" width="100%"/>
      <div><strong>losses</strong></div>
    </td>
  </tr>
</table>


