import streamlit as st
from solver import solve_statistics, solve_binomial, solve_z_score_from_sample, solve_t_test

def run_stat_solver():
    st.header("📊 Statistical Solver")

    st.markdown("Select a topic to solve:")
    option = st.selectbox("Choose topic", [
        "Descriptive Statistics",
        "Binomial Probability",
        "Z-Score from Sample",
        "T-Test"
    ])

    if option == "Descriptive Statistics":
        data = st.text_input("Enter numbers separated by commas:")
        if data:
            numbers = [float(x) for x in data.split(',')]
            result = solve_statistics(numbers)
            st.write(result)

    elif option == "Binomial Probability":
        n = st.number_input("Number of trials (n)", min_value=1, step=1)
        p = st.number_input("Probability of success (p)", min_value=0.0, max_value=1.0)
        x = st.number_input("Number of successes (x)", min_value=0, step=1)
        if st.button("Calculate Binomial Probability"):
            result = solve_binomial(n, p, x)
            st.write(result)

    elif option == "Z-Score from Sample":
        x = st.number_input("Sample Mean")
        mu = st.number_input("Population Mean")
        sigma = st.number_input("Standard Deviation")
        n = st.number_input("Sample Size", min_value=1, step=1)
        if st.button("Calculate Z-Score"):
            result = solve_z_score_from_sample(x, mu, sigma, n)
            st.write(result)

    elif option == "T-Test":
        x_bar = st.number_input("Sample Mean (x̄)")
        mu = st.number_input("Population Mean (μ)")
        s = st.number_input("Sample Std Dev (s)")
        n = st.number_input("Sample Size (n)", min_value=1, step=1)
        if st.button("Calculate T-Test"):
            result = solve_t_test(x_bar, mu, s, n)
            st.write(result)
