# Facial Emotion Detection Web App 😃  

This project is a **Flask-based web application** that detects human emotions from uploaded facial images using a **Convolutional Neural Network (CNN)** trained on the [Face Expression Recognition Dataset](https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset/data).  

The application allows users to **upload an image**, and it predicts the emotion with a **confidence score**, while displaying the processed image on the webpage.  

---

## 🚀 Features
- Upload a facial image through the web interface  
- Deep learning model predicts the emotion:  
  - Happy  
  - Sad  
  - Angry  
  - Surprise  
  - Neutral  
  - Fear  
  - Disgust  
- Displays confidence score (%)  
- Responsive and clean **Bootstrap UI**  
- Built with **Flask (backend)** and **HTML/CSS (frontend)**  

---

## 📂 Dataset
We trained the model using the [Face Expression Recognition Dataset](https://www.kaggle.com/datasets/jonathanoheix/face-expression-recognition-dataset/data).  

- Contains **48x48 grayscale images** of faces.  
- 7 Emotion classes available.  

---

## 🚀 Tech Stack

### 🔹 Backend
- **Python 3.8+**
- **Flask** → Web framework for routing and handling requests
- **TensorFlow / Keras** → Deep Learning model for facial emotion recognition
- **NumPy** → Array operations and preprocessing
- **OS** → File handling and uploads

### 🔹 Frontend
- **HTML5** → Webpage structure
- **CSS3** → Custom styling (gradient, hover effects, UI design)
- **Bootstrap 5** → Responsive design and form styling
- **Jinja2** → Template rendering for Flask (displaying results dynamically)

---
