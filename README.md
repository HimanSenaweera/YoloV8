# 🚗 Object Detection (YOLO) 

This project contains a trained Yolo11n model for vehicle number plate detection and for this project I downloaded the dataset and annotated it manually.

Dataset Source: [Open Images Dataset – Vehicle Number Plates](https://storage.googleapis.com/openimages/web/visualizer/index.html?type=detection&set=train&c=%2Fm%2F01jfm_)
Annotation Tool: [CVAT (Computer Vision Annotation Tool)](https://www.cvat.ai/)

---
## 👁️ Demo

<table>
  <tr>
    <td style="text-align:center;">
      <img src="train_batch0.jpg" alt="Original image" width="100%"/>
      <div><strong>Training set</strong></div>
    </td>
    <td style="text-align:center;">
      <img src="val_batch0_labels.jpg" alt="Blurred image" width="100%"/>
      <div><strong>Validation set</strong></div>
    </td>
  </tr>
</table>


<table>
  <tr>
    <td style="text-align:center;">
      <img src="confusion_matrix_normalized.png" alt="Blurred image" width="100%"/>
      <div><strong>Original</strong></div>
    </td>
    <td style="text-align:center;">
      <img src="results.png" alt="Original image" width="100%"/>
      <div><strong>Blurred</strong></div>
    </td>
  </tr>
</table>
