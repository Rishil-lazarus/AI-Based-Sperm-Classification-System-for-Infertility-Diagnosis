# AI-Based-Sperm-Classification-System-for-Infertility-Diagnosis
Built an AI-based sperm classification system using a custom CNN to categorize sperm images into normal, abnormal, and non-sperm. Preprocessed and augmented data from the SMIDS dataset. Deployed as a Flask web app with a dark-themed UI for real-world infertility diagnosis support.

## 🚀 Live Demo

🔗 Web App: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📂 Dataset

- **Dataset Name**: Sperm Morphology Image Data Set (SMIDS)  
- **Source**: [Kaggle - SMIDS Dataset](https://www.kaggle.com/datasets/orvile/sperm-morphology-image-data-set-smids)  
- **Classes**:
  - Normal Sperm (1021 images)
  - Abnormal Sperm (1005 images)
  - Non-Sperm Objects (947 images)

---

## 🛠️ Features

- 🧠 Trained custom CNN model from scratch (no pre-trained models)
- 🔄 Advanced image augmentation (rotation, shift, zoom, flip, etc.)
- 🎯 Multi-class classification: Normal Sperm, Abnormal Sperm, Non-Sperm
- 📊 Evaluation metrics: Accuracy, Precision, Recall, F1-score
- 🌐 Flask-based web app with a modern dark theme UI
- ⚙️ Optimized for real-world generalization and deployment

---

## 🏗️ Project Structure

---

## 🧪 Model Performance

### 🔬 Class-wise Metrics

| Class            | Precision | Recall | F1-Score | Support |
|------------------|-----------|--------|----------|---------|
| Abnormal Sperm   | 0.81      | 0.55   | 0.66     | 402     |
| Non-Sperm        | 0.97      | 0.79   | 0.87     | 390     |
| Normal Sperm     | 0.63      | 0.95   | 0.76     | 409     |

### 📊 Overall Metrics

| Metric           | Score     |
|------------------|-----------|
| **Accuracy**     | 0.76      |
| **Macro Avg**    | Precision: 0.80<br>Recall: 0.76<br>F1-Score: 0.76 |
| **Weighted Avg** | Precision: 0.80<br>Recall: 0.76<br>F1-Score: 0.76 |

> 📈 The model performs best on **Non-Sperm** and **Normal Sperm**, with improvements planned for **Abnormal Sperm** detection.

---

## 💻 Tech Stack

- Python 3.12.4
- TensorFlow & Keras
- OpenCV
- NumPy, Matplotlib, Scikit-learn
- Flask (for web deployment)
- HTML/CSS (dark-themed frontend)

---

## 📦 Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/sperm-classification.git
   cd sperm-classification



---

Let me know if you want this as a downloadable `.md` file or if you'd like help uploading this to your GitHub repo!

