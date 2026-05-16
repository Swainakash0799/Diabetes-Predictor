# Diabetes Prediction using Machine Learning

* A machine learning project that predicts the likelihood of diabetes using clinical health data. This project implements and compares Logistic Regression and Support Vector Machine (SVM) models to identify the best-performing approach.
---

## 🚀 Live Demo
🔗 [Click here to use the app](https://diabetes-predictor-0799.streamlit.app/)

---

## 📌 Project Highlights

* 🔍 Built a binary classification model for medical diagnosis
* ⚙️ Implemented a complete end-to-end ML pipeline
* 🤖 Compared Logistic Regression vs SVM
* 📊 Evaluated using Accuracy, Precision, Recall, F1-score & ROC Curve
* 🧪 Focused on real-world healthcare application

---

## 🎯 Problem Statement

Early detection of diabetes is crucial to prevent severe health complications.
This project aims to develop a machine learning model that can **predict whether a patient is diabetic or not** based on diagnostic measurements.

---

## 📊 Dataset Details

* 📁 **Dataset:** http://kaggle.com/datasets/saurabh00007/diabetescsv
* 🎯 **Target Variable:** `Outcome`

  * `0` → Non-diabetic
  * `1` → Diabetic

### 🔑 Key Features:

* Glucose Level
* Body Mass Index (BMI)
* Age
* Blood Pressure
* Insulin Level
* Skin Thickness

---

## ⚙️ Tech Stack

| Category      | Tools Used              |
| ------------- | ------------------------|
| Language      | Python                  |
| Data Handling | Pandas, NumPy           |
| ML Model      | Logistic Regression,SVM |               
| Visualization | Matplotlib              |
| Deployment    | Streamlit               |
| ML Library    | Scikit-learn            |

---

## 🔍 Workflow

Data Collection → Data Cleaning → Feature Selection → Train-Test Split  
→ Feature Scaling → Model Training → Evaluation → Comparison → Deployment

---

## 🤖 Models Used
* Logistic Regression
  - Simple and efficient for binary classification
  - Works well with linearly separable data
* Support Vector Machine (SVM)
  - Effective in high-dimensional spaces
  - Can capture complex decision boundaries
  - Better performance in this project

## 📈 Model Performance

| Metric            | Logistic Regression | SVM |
| ----------------- | --------------------|-----|
| Training Accuracy | 78%                 | 78% |
| Testing Accuracy  | 76%                 | 77% |

### 📊 Key Insight:

* SVM achieved higher accuracy than Logistic Regression
* Logistic Regression is simpler and more interpretable
* Feature scaling improved both models
* SVM captures complex patterns better
* No significant overfitting observed

---

## 📊 Evaluation Metrics Used

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC Curve

---

## 🧠 Key Learnings

* Importance of feature scaling in ML models
* Understanding model comparison and selection
* Difference between **accuracy vs recall in healthcare models**
* How to evaluate models beyond accuracy
* End-to-end ML project workflow

---


