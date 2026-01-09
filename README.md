# 🧠 Student Focus & Burnout Risk Predictor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green)
![Streamlit](https://img.shields.io/badge/App-Streamlit-red)

A beginner-friendly Machine Learning project that predicts a student's risk of **burnout** (Low, Medium, High) based on their daily habits like study hours, sleep, screen time, and stress levels.

## 🌟 Project Overview

This project simulates a realistic dataset of student habits and trains a **Random Forest Classifier** to predict burnout risk. It includes a complete **Jupyter Notebook** for the data verification/training process and a **Streamlit Web Application** for an interactive demo.

### Key Features
*   **Data Simulation**: Generates 500+ realistic synthetic student records.
*   **Exploratory Data Analysis (EDA)**: Visualizes relationships between stress, sleep, and burnout using Matplotlib & Seaborn.
*   **Machine Learning**: Trains a Random Forest model with high accuracy.
*   **Interactive Web App**: A user-friendly interface to test the model in real-time.

## 📂 Project Structure

```
├── student_burnout_predictor.ipynb  # Jupyter Notebook (Data Analysis & Model Training)
├── app.py                           # Streamlit Web Application
├── requirements.txt                 # List of dependencies
└── README.md                        # Project Documentation
```

## 🛠️ Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/student-burnout-predictor.git
    cd student-burnout-predictor
    ```

2.  **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 How to Run

### Option 1: The Web App (Recommended)
Launch the interactive dashboard to predict your own risk score.
```bash
streamlit run app.py
```

### Option 2: The Jupyter Notebook
Explore the data creation, EDA, and model training steps.
```bash
jupyter notebook student_burnout_predictor.ipynb
```

## 🧠 How It Works

The model considers the following features:
*   **Study Hours**: Daily hours spent studying.
*   **Sleep Hours**: Daily hours of sleep.
*   **Screen Time**: Daily hours on phone/laptop.
*   **Exercise**: Minutes of physical activity.
*   **Stress Level**: Self-reported stress on a scale of 1-10.
*   **Attendance**: Percentage of class attendance.

Based on these inputs, the model classifies the risk into:
*   🟢 **Low Risk**: Healthy balance.
*   🟠 **Medium Risk**: Warning signs present.
*   🔴 **High Risk**: Immediate break recommended.

## 📊 Example Visualization
*(You can add a screenshot of your charts here)*

## 🤝 Contributing
Feel free to fork this repository and improve the model! Some ideas:
*   Add more features like "Part-time Job" or "Commute Time".
*   Try different algorithms like SVM or Gradient Boosting.

## 📜 License
This project is open-source and available under the MIT License.
