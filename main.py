import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO
from reportlab.pdfgen import canvas
import openai
from dotenv import load_dotenv
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Hide Streamlit UI
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

from solver import (
    solve_statistics,
    solve_binomial,
    solve_z_score_from_sample,
    solve_t_test,
    chi_square_goodness,
    chi_square_independence
)
from explain import (
    explain_statistics,
    explain_binomial,
    explain_z_score,
    explain_t_test,
    explain_chi_square
)
from ai_chatbot import run_ai_chatbot
from stat_solver import run_stat_solver
from ml_playground import run_ml_playground
from probability_calculator import run_probability_calculator

# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.markdown(r"""<style>.katex { font-size: 1.2em; }</style>""", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

# Sidebar
page = st.sidebar.selectbox("📚 Select Page", [
    "Stat Solver", "Mini ML Playground", "Live Probability Calculator", "AI Stat Tutor Chatbot"
])

if st.sidebar.checkbox("🎯 Quiz Mode"):
    def quiz_mode():
        st.title("🧠 Quiz Mode - Test Your Stats Knowledge")
        questions = [
            {"question": "What does standard deviation measure?", "options": ["Central tendency", "Skewness", "Spread of data", "Sample size"], "answer": "Spread of data"},
            {"question": "Which distribution is symmetric and bell-shaped?", "options": ["Poisson", "Normal", "Binomial", "Uniform"], "answer": "Normal"},
            {"question": "In statistics, what does 'n' usually represent?", "options": ["Mean", "Variance", "Sample size", "Probability"], "answer": "Sample size"},
            {"question": "Which test checks independence in categorical data?", "options": ["Z-Test", "Chi-Square", "T-Test", "ANOVA"], "answer": "Chi-Square"},
            {"question": "What value does a perfectly normal distribution’s skewness have?", "options": ["0", "1", "Negative", "Undefined"], "answer": "0"},
            {"question": "If variance is 0, what can we say about the data?", "options": ["All values are different", "There are many outliers", "All values are the same", "It is a normal distribution"], "answer": "All values are the same"},
            {"question": "What is the area under the standard normal curve?", "options": ["0", "0.5", "1", "Depends on data"], "answer": "1"},
            {"question": "Which of the following is NOT a measure of central tendency?", "options": ["Mean", "Median", "Mode", "Standard deviation"], "answer": "Standard deviation"},
            {"question": "What is the formula for variance?", "options": ["Σ(x̄ - x)/n", "Σ(x - x̄)^2 / n", "Σx / n", "x̄^2 / n"], "answer": "Σ(x - x̄)^2 / n"},
            {"question": "Which probability is impossible?", "options": ["0", "0.5", "1", "1.5"], "answer": "1.5"},
            {"question": "What does a P-value less than 0.05 typically indicate?", "options": ["Accept null hypothesis", "Strong evidence against null", "Data error", "Random chance"], "answer": "Strong evidence against null"},
            {"question": "What shape is a normal distribution?", "options": ["Skewed", "Bell curve", "J-shaped", "Uniform"], "answer": "Bell curve"},
            {"question": "What does the mean represent?", "options": ["Middle value", "Most frequent value", "Average", "Difference between max and min"], "answer": "Average"},
            {"question": "What is the default degrees of freedom in sample standard deviation?", "options": ["n", "n-1", "n+1", "1"], "answer": "n-1"},
            {"question": "Which test is used for comparing means of two samples?", "options": ["Chi-Square", "T-Test", "Z-Test", "ANOVA"], "answer": "T-Test"},
            {"question": "Which distribution is used for large sample sizes?", "options": ["T-distribution", "Z-distribution", "Poisson", "F-distribution"], "answer": "Z-distribution"},
            {"question": "Which is a qualitative variable?", "options": ["Age", "Height", "Color", "Weight"], "answer": "Color"},
            {"question": "Which test is suitable for small sample sizes?", "options": ["Z-Test", "Chi-Square", "T-Test", "ANOVA"], "answer": "T-Test"},
            {"question": "What is the median of this set: 10, 20, 30, 40, 50?", "options": ["30", "25", "20", "35"], "answer": "30"},
            {"question": "What is the mode of this set: 2, 3, 4, 3, 5?", "options": ["2", "3", "4", "5"], "answer": "3"},
            {"question": "Which graph is best to visualize distribution?", "options": ["Histogram", "Bar Chart", "Pie Chart", "Line Graph"], "answer": "Histogram"},
            {"question": "Which value is most resistant to outliers?", "options": ["Mean", "Median", "Mode", "Standard Deviation"], "answer": "Median"}
        ]
        score = 0
        for i, q in enumerate(questions):
            st.subheader(q["question"])
            choice = st.radio("Choose an answer:", q["options"], key=f"quiz_q_{i}")
            if st.button(f"Submit Answer {i+1}", key=f"submit_{i}"):
                if choice == q["answer"]:
                    st.success("✅ Correct!")
                    score += 1
                else:
                    st.error(f"❌ Wrong! Correct answer: {q['answer']}")
        st.write(f"### 🏁 Your Final Score: {score}/{len(questions)} ✅")

    quiz_mode()

elif page == "Mini ML Playground":
    run_ml_playground()
elif page == "Live Probability Calculator":
    run_probability_calculator()
elif page == "AI Stat Tutor Chatbot":
    run_ai_chatbot()
else:
    # Combined Stat Solver
    st.title("📊 StatProTutor")
    st.write("This app helps you learn Statistics and Probability easily.")
    topic = st.selectbox("Choose a topic", [
        "Mean, Variance, Std Dev", "Binomial Probability", "Z-Score", "T-Test", "Chi-Square Test"
    ])

    def plot_graphs(data):
        fig, axs = plt.subplots(1, 2, figsize=(12, 4))
        sns.histplot(data, kde=True, ax=axs[0])
        axs[0].set_title("Histogram")
        sns.boxplot(x=data, ax=axs[1])
        axs[1].set_title("Boxplot")
        st.pyplot(fig)

    if topic == "Mean, Variance, Std Dev":
        st.subheader("📊 Mean, Variance, and Standard Deviation")
        input_data = st.text_input("Enter comma-separated numbers (e.g., 10, 20, 30):")
        if input_data:
            try:
                numbers = [float(x.strip()) for x in input_data.split(",")]
                mean_val = np.mean(numbers)
                var_val = np.var(numbers)
                std_val = np.std(numbers)
                st.success("✅ Results:")
                st.write(f"Mean : {mean_val:.2f}")
                st.write(f"Variance : {var_val:.2f}")
                st.write(f"Standard Deviation : {std_val:.2f}")
                plot_graphs(numbers)
            except:
                st.error("❌ Invalid input! Use comma-separated numbers.")

    elif topic == "Binomial Probability":
        st.subheader("📌 Binomial Probability Calculator")
        n = st.number_input("🔢 Number of Trials (n)", min_value=0, step=1, value=10)
        p = st.number_input("🎲 Probability of Success (p)", min_value=0.0, max_value=1.0, step=0.01, value=0.5)
        k = st.number_input("✅ Number of Successes (k)", min_value=0, step=1, value=5)
        if st.button("Calculate"):
            try:
                result = solve_binomial(n, p, k)
                st.success(f"📊 Probability Result: {result['binomial_prob']:.4f}")
                st.markdown(explain_binomial(n))
            except Exception as e:
                st.error(f"❌ Error: {e}")

    elif topic == "Z-Score":
        st.subheader("📉 Z-Score Calculator")
        data_input = st.text_input("Enter sample data (comma-separated)", "10, 20, 30, 40")
        target = st.number_input("🎯 Target Value (X):", value=25.0)
        if st.button("Calculate Z-Score"):
            try:
                values = [float(x.strip()) for x in data_input.split(",")]
                mean = np.mean(values)
                std = np.std(values, ddof=1)
                z = (target - mean) / (std / np.sqrt(len(values)))
                st.success(f"📈 Z-score: {z:.4f}")
                st.info(f"Mean = {mean:.2f}, Std Dev = {std:.2f}, N = {len(values)}")
                plot_graphs(values)
                st.markdown(explain_z_score(values, target))
            except Exception as e:
                st.error(f"❌ Error: {e}")

    elif topic == "T-Test":
        st.subheader("🧪 One-Sample T-Test")
        data_input = st.text_input("Enter sample values (comma-separated):", "10, 20, 30")
        pop_mean = st.number_input("Population Mean", value=20.0)
        if st.button("Run T-Test"):
            try:
                values = [float(x.strip()) for x in data_input.split(",")]
                t_stat, p_val = solve_t_test(values, pop_mean)
                st.success(f"T-statistic: {t_stat:.4f}, P-value: {p_val:.4f}")
                plot_graphs(values)
                st.markdown(explain_t_test(values, pop_mean))
            except Exception as e:
                st.error(f"❌ Error: {e}")

    elif topic == "Chi-Square Test":
        st.subheader("📐 Chi-Square Test")
        test_type = st.selectbox("Choose Test Type", ["Goodness of Fit", "Test of Independence"])
        if test_type == "Goodness of Fit":
            obs = st.text_input("Observed Frequencies (comma-separated)", "50,30,20")
            exp = st.text_input("Expected Frequencies (comma-separated)", "40,40,20")
            if st.button("Run GoF Test"):
                try:
                    observed = np.array([int(x) for x in obs.split(",")])
                    expected = np.array([int(x) for x in exp.split(",")])
                    result = chi_square_goodness(observed, expected)
                    st.markdown(explain_chi_square(result))
                except Exception as e:
                    st.error(f"❌ Error: {e}")
        else:
            matrix = st.text_area("Contingency Table (CSV format)", "10,20\n30,40")
            if st.button("Run Independence Test"):
                try:
                    data = np.array([[int(x) for x in row.split(",")] for row in matrix.strip().split("\n")])
                    result = chi_square_independence(data)
                    st.markdown(explain_chi_square(result))
                except Exception as e:
                    st.error(f"❌ Error: {e}")

