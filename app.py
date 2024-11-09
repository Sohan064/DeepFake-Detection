from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import os

app = Flask(__name__)
model = load_model("model/deepfake_model.h5")  # Load your trained model

def preprocess_image(image):
    # Preprocess image to match model input
    image = cv2.resize(image, (224, 224))
    image = image.astype("float32") / 255.0
    image = np.expand_dims(image, axis=0)
    return image

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["image"]
    if file:
        # Read the image file
        image = np.fromstring(file.read(), np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        
        # Preprocess and classify
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)
        
        # Interpret the result
        result = "Fake" if prediction >= 0.5 else "Real"
        return result
    else:
        return "No file uploaded", 400

if __name__ == "__main__":
    app.run(debug=True)