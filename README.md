# Food-101 Image Classifier 🍔🍰

A deep learning image classifier that identifies 101 different food dishes from a photo, built with TensorFlow/Keras and deployed as a live web app.

## 🔗 Live Demo
foodclassification-kvcdyhy5gecvkpdsbqjk55.streamlit.app

Upload any food photo and get an instant prediction with confidence score.

## 📊 Model
- Architecture: MobileNetV2 (transfer learning from ImageNet)
- Approach: Frozen-base training with data augmentation, followed by fine-tuning the top layers at a low learning rate
- Dataset: Food-101 — 101 food classes, ~101,000 images
- Test accuracy: 66%

## 🛠️ Tech Stack
- TensorFlow / Keras
- Streamlit (deployment)
- Trained on Google Colab (T4 GPU)

## 📁 Files
- app.py — Streamlit web app
- food101_mobilenetv2.keras — trained model
- classes.json — class label mapping
- requirements.txt — dependencies

## 🚀 Run Locally
pip install -r requirements.txt
streamlit run app.py

## 📈 Training Notes
- Started with a frozen MobileNetV2 base — overfit quickly (train/val accuracy gap widened, val loss rose)
- Added data augmentation (random flip, rotation, zoom) — fixed the overfitting, val accuracy tracked train accuracy closely
- Fine-tuned the top 30 layers of the base model at lr=1e-5 — boosted accuracy from ~54% to 66%

## 🔮 Possible Improvements
- Larger backbone (EfficientNet) for higher accuracy
- Top-3 prediction display instead of top-1
- More fine-tuning epochs
