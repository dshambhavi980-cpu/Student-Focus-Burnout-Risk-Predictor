import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Page Config
st.set_page_config(page_title="Burnout Predictor", page_icon="🧠")
st.title("🧠 Student Focus & Burnout Risk Predictor")
st.write("Enter your daily habits below to see your predicted burnout risk level.")

# --- TRAIN MODEL DIRECTLY IN APP TO PREVENT VERSION ERRORS ---
@st.cache_resource
def train_model():
    # Simulate Data (Same as Notebook)
    np.random.seed(42)
    n_samples = 500
    study_hours = np.random.randint(1, 10, n_samples)
    sleep_hours = np.random.randint(4, 10, n_samples)
    screen_time = np.random.randint(1, 12, n_samples)
    exercise_minutes = np.random.randint(0, 120, n_samples)
    attendance = np.random.randint(50, 100, n_samples)
    
    stress_level = []
    for i in range(n_samples):
        base_stress = 5
        if sleep_hours[i] < 6: base_stress += 2
        if study_hours[i] > 7: base_stress += 1
        if screen_time[i] > 8: base_stress += 1
        if exercise_minutes[i] > 60: base_stress -= 2
        final_stress = base_stress + np.random.randint(-2, 3)
        stress_level.append(max(1, min(10, final_stress)))
    
    stress_level = np.array(stress_level)
    
    data = pd.DataFrame({
        'Study Hours': study_hours,
        'Sleep Hours': sleep_hours,
        'Screen Time': screen_time,
        'Exercise Min': exercise_minutes,
        'Stress (1-10)': stress_level,
        'Attendance %': attendance
    })
    
    def calculate_burnout(row):
        score = 0
        score += row['Stress (1-10)'] * 1.5
        score += row['Screen Time'] * 0.5
        score += (10 - row['Sleep Hours']) * 1.0
        score -= (row['Exercise Min'] / 60) * 0.5
        if score > 15: return 'High'
        elif score > 10: return 'Medium'
        else: return 'Low'

    data['Burnout Risk'] = data.apply(calculate_burnout, axis=1)
    
    X = data.drop('Burnout Risk', axis=1)
    y = data['Burnout Risk']
    
    # Train Model
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    return clf

# Load the model (trains once and caches it)
model = train_model()

# --- INPUT FORM ---
with st.form("prediction_form"):
    st.header("Your Daily Habits")
    col1, col2 = st.columns(2)
    
    with col1:
        study = st.slider("Hours Studied per Day", 0, 16, 6)
        sleep = st.slider("Hours of Sleep", 0, 12, 7)
        screen = st.slider("Screen Time (Hours)", 0, 16, 6)
        
    with col2:
        exercise = st.number_input("Exercise Minutes per Day", 0, 180, 45)
        stress = st.slider("Stress Level (1-10)", 1, 10, 5)
        attendance = st.slider("Class Attendance %", 0, 100, 90)
        
    submit_button = st.form_submit_button("Predict Risk 🚀")

# --- PREDICTION ---
if submit_button:
    feature_columns = ['Study Hours', 'Sleep Hours', 'Screen Time', 'Exercise Min', 'Stress (1-10)', 'Attendance %']
    input_data = pd.DataFrame([[study, sleep, screen, exercise, stress, attendance]], columns=feature_columns)
    
    prediction = model.predict(input_data)[0]
    
    st.markdown("---")
    st.subheader("Results:")
    if prediction == "Low":
        st.success(f"✅ Low Risk: You are maintaining a healthy balance! Keep it up.")
        st.balloons()
    elif prediction == "Medium":
        st.warning(f"⚠️ Medium Risk: You might be pushing yourself. Try to rest more or reduce screen time.")
    else:
        st.error(f"🔥 High Risk: PLEASE TAKE A BREAK! Your burnout risk is high.")
