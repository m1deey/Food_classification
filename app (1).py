import streamlit as st
import tensorflow as tf
import numpy as np
import json
from PIL import Image

@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("food101_mobilenetv2.keras")
    with open("classes.json") as f:
        classes = json.load(f)
    return model, classes

model, classes = load_model()

st.title("Food-101 Classifier")
st.write("Upload a food image and get the predicted dish.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    img = image.resize((224, 224))
    img_array = np.array(img)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_class = classes[np.argmax(predictions)]
    confidence = np.max(predictions) * 100

    st.subheader(f"Prediction: {predicted_class.replace('_', ' ').title()}")
    st.write(f"Confidence: {confidence:.2f}%")
