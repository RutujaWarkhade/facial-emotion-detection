from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Load the trained model (absolute path)
MODEL_PATH = r"D:\Emotion Detection\facial_emotion_detection_model.h5"
model = load_model(MODEL_PATH)

# Define class names
class_names = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

# Upload folder (inside static/uploads so Flask can serve images)
UPLOAD_FOLDER = r"D:\Emotion Detection\static\uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Emotion detection function
def detect_emotion(img_path):
    img = image.load_img(img_path, target_size=(48, 48), color_mode='grayscale')
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    predicted_index = np.argmax(prediction)
    predicted_class = class_names[predicted_index]
    confidence = round(prediction[0][predicted_index] * 100, 2)

    return predicted_class, confidence

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file uploaded!'
        file = request.files['file']
        if file.filename == '':
            return 'No file selected!'

        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            # Detect emotion
            emotion, confidence = detect_emotion(file_path)

            # Relative path for HTML (Flask serves from /static/)
            display_path = "static/uploads/" + file.filename

            return render_template('index.html', image_path=display_path, emotion=emotion, confidence=confidence)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
