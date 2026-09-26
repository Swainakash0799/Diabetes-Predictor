# Diabetes Prediction System 

A machine learning project that predicts the likelihood of diabetes using clinical health data. This project implements and compares Logistic Regression and Support Vector Machine (SVM) models to identify the best-performing approach.

🌐 **Live Demo:** https://diabetes-predictor-007.streamlit.app/

---

## 📌 Project Highlights

- Built a binary classification model for medical diagnosis
- Implemented a complete end-to-end ML pipeline
- Compared Logistic Regression vs SVM
- Evaluated using Accuracy, Precision, Recall, F1-score & ROC Curve
- Focused on real-world healthcare application

---

## 🎯 Problem Statement

Early detection of diabetes is crucial to prevent severe health complications. This project aims to develop a machine learning model that can predict whether a patient is diabetic or not based on diagnostic measurements.

---

## 📊 Dataset Details

📁 Dataset: http://kaggle.com/datasets/saurabh00007/diabetescsv

🎯 Target Variable: Outcome

* 0 → Non-diabetic
* 1 → Diabetic

### 🔑 Key Features:

* Glucose Level
* Body Mass Index (BMI)
* Age
* Blood Pressure
* Insulin Level
* Skin Thickness

---

## ⚙️ Tech Stack

| Category      | Tools Used               |
| ------------- | ------------------------ |
| Language      | Python                   |
| Data Handling | Pandas, NumPy            |
| ML Model      | Logistic Regression, SVM |
| Visualization | Matplotlib               |
| Deployment    | Streamlit                |
| ML Library    | Scikit-learn             |

---

## 🔍 Workflow

Data Collection → Data Cleaning → Feature Selection → Train-Test Split
→ Feature Scaling → Model Training → Evaluation → Comparison → Deployment

---

## 🤖 Models Used

### Logistic Regression

* Simple and efficient for binary classification
* Works well with linearly separable data
* Provides probability outputs (`predict_proba`)

### Support Vector Machine (SVM)

* Effective in high-dimensional spaces
* Captures complex decision boundaries
* Achieved slightly higher accuracy in this project

---

## ⚙️ Model Selection Strategy

Although **SVM achieved slightly higher accuracy**, **Logistic Regression was selected for deployment** due to:

* Provides **probability-based output** (risk percentage)
* More **interpretable**, which is important in healthcare
* Faster for real-time web applications

---

## 📈 Model Performance

| Metric            | Logistic Regression | SVM |
| ----------------- | ------------------- | --- |
| Training Accuracy | 78%                 | 78% |
| Testing Accuracy  | 76%                 | 77% |

### 📊 Key Insights:

* SVM achieved slightly higher accuracy
* Logistic Regression is simpler and more interpretable
* Feature scaling improved both models
* No significant overfitting observed

---

## 🔄 Deployment Pipeline 

During training, data was scaled before model learning:

**Training Pipeline:**
Input Data → Feature Scaling → Model Training

During deployment, the same transformation is applied:

**Prediction Pipeline:**
User Input → Scaler → Model → Prediction

### Why both files are used:

* `logistic_scaler.pkl` → ensures input is scaled like training data
* `logistic_model.pkl` → performs prediction

This prevents **training-serving mismatch**, ensuring accurate and consistent predictions.

---

## ▶️ Run Locally

### 1. Clone the repository

```
git clone https://github.com/Swainakash0799/Diabetes-Predictor.git
cd Diabetes-Predictor
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Run the app

```
streamlit run app.py
```


## 📊 Evaluation Metrics Used

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

---

## 🧠 Key Learnings

* Importance of feature scaling in ML models
* Understanding model comparison and selection
* Difference between accuracy vs recall in healthcare
* Handling real-world deployment issues (pipeline mismatch)
* End-to-end ML project workflow

---

# 👨‍💻 Author

**Akash Swain**
