# Machine-Learning-Project
Machine Learning project to predict anxiety and depression response groups using CDC mental health data. Includes model training, evaluation, and Streamlit app deployment.
# Anxiety & Depression Prediction using Machine Learning

This project applies supervised machine learning to classify mental health survey responses into two groups (early and late), based on indicators of anxiety or depression.

---

##  Problem Statement

Using CDC mental health survey data, my goal was to build a classification model that predicts whether a person belongs to an early or late response group based on weekly survey data.

---

##  Dataset

- Source: [CDC Mental Health Indicators]
- Features used:
  - `Subgroup` (categorical demographic variable)
  - `Value` (percentage reporting mental health symptoms)
  - `Time Period` (week number)
- Target Variable: `Group_Label` (0 for weeks 11–25, 1 for weeks 26–52)

---

##  Preprocessing

- Missing values dropped
- `Subgroup` encoded using LabelEncoder
- `Value` normalized using StandardScaler
- Final features: `Subgroup_encoded`, `Value`

---

##  Models Trained

| Model              | Accuracy | Precision | Recall | F1 Score | AUC  |
|-------------------|----------|-----------|--------|----------|------|
| Logistic Regression | 0.78     | 0.70      | 0.68   | 0.69     | 0.80 |
| **Random Forest** (Final Model) | **0.84** | **0.83** | **0.81** | **0.82** | **0.89** |
| XGBoost            | 0.89     | 0.88      | 0.87   | 0.875    | 0.94 |

Final model selected: **Random Forest**

---

##  Deployment

Deployed using Streamlit. The app allows users to input:
- Subgroup
- Value
- Time Period

And returns a prediction: Group 0 (early) or Group 1 (late).

---

##  Files in this Repo

- `habiba final.ipynb`: Jupyter notebook with complete ML workflow
- `app.py`: Streamlit app script
- `train_model.py`: Model training script
- `model.zip`: Final trained Random Forest model (compressed)
- `scaler.pkl`: StandardScaler used in preprocessing
- `encoder.pkl`: LabelEncoder used on Subgroup
- `Indicators_of_Anxiety_or_Depression.csv`: Dataset
- `README.md`: This file



---

##  Video Explanation

Watch the complete explanation here:  
🎬 [Project Presentation Video](https://nileuniversity-my.sharepoint.com/:v:/g/personal/h_khaled2124_nu_edu_eg/ESaRZwlB4S5NnG4cbJK2VtcB6eBf8hvPFBjx7V9-V5LFzA?e=jOlQ0K)

---

## Acknowledgments

Thanks to Dr. Mohamed El Sayeh for his guidance throughout the course.
