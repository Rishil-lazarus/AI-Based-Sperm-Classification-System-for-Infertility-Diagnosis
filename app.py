from flask import Flask, render_template, request
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

model = tf.keras.models.load_model(r"C:\Users\User\Documents\sperm_project\SMIDS\_sperm_classification_.keras")

CLASS_LABELS = ["Abnormal Sperm", "Non-Sperm", "Normal Sperm"]

def predict_image(img_path):
    img = image.load_img(img_path, target_size=(256, 256))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    prediction = model.predict(img_array)[0]
    predicted_class = np.argmax(prediction)
    confidence = prediction[predicted_class] * 100

    return CLASS_LABELS[predicted_class], round(confidence, 2)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    file_path = None
    predicted_class = None
    confidence = None

    if request.method == "POST":
        file = request.files.get("file")
        if file and file.filename:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)
            predicted_class, confidence = predict_image(file_path)

    return render_template("predict.html", image_url=file_path, 
                           prediction=predicted_class, confidence=confidence)

if __name__ == "__main__":
    app.run(debug=True)
