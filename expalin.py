import numpy as np

# Explanation for Mean, Variance, and Std Dev
def explain_statistics(data):
    arr = np.array(data)
    n = len(arr)
    mean = np.mean(arr)
    variance = np.var(arr)
    std_dev = np.std(arr)

    explanation = f"""
### 📊 Mean, Variance, and Standard Deviation Explanation

**Step 1: Calculate the Mean (μ)**  
Mean = (Sum of all values) / (Number of values)  
= {np.sum(arr)} / {n}  
= **{mean:.2f}**

**Step 2: Calculate the Variance (σ²)**  
Variance = Σ(xᵢ - μ)² / n  
= {variance:.2f}

**Step 3: Calculate the Standard Deviation (σ)**  
Standard Deviation = √Variance  
= √{variance:.2f}  
= **{std_dev:.2f}**
"""
    return explanation

# Explanation for Binomial Probability
def explain_binomial(n, p=None):
    explanation = f"""
### 📌 Binomial Probability Explanation

We use the formula:  
**P(X = k) = C(n, k) * p^k * (1 - p)^(n - k)**

Where:  
- `n` = number of trials = **{n}**  
- `p` = probability of success (given)  
- `k` = number of successful outcomes

This gives us the **exact probability** of getting exactly `k` successes out of `n` trials.
"""
    return explanation

# Explanation for Z-Score
def explain_z_score(values, x):
    arr = np.array(values)
    n = len(arr)
    mean = np.mean(arr)
    std = np.std(arr, ddof=1)
    z = (x - mean) / (std / np.sqrt(n))

    explanation = f"""
### 📉 Z-Score Explanation

**Z = (X - μ) / (σ / √n)**  
Where:  
- `X` = target value = {x}  
- `μ` = mean of sample = {mean:.2f}  
- `σ` = sample standard deviation = {std:.2f}  
- `n` = sample size = {n}  

**Z = ({x} - {mean:.2f}) / ({std:.2f} / √{n}) = {z:.4f}**

This Z-score tells how many standard errors the value `{x}` is from the sample mean.
"""
    return explanation

# Explanation for T-Test
def explain_t_test(values, pop_mean):
    arr = np.array(values)
    n = len(arr)
    sample_mean = np.mean(arr)
    sample_std = np.std(arr, ddof=1)
    t_stat = (sample_mean - pop_mean) / (sample_std / np.sqrt(n))

    explanation = f"""
### 🧪 T-Test Explanation (One Sample)

**T = (x̄ - μ) / (s / √n)**  
Where:  
- `x̄` = sample mean = {sample_mean:.2f}  
- `μ` = population mean = {pop_mean}  
- `s` = sample standard deviation = {sample_std:.2f}  
- `n` = sample size = {n}  

**T = ({sample_mean:.2f} - {pop_mean}) / ({sample_std:.2f} / √{n}) = {t_stat:.4f}**

This T-statistic tells how far the sample mean is from the population mean in standard error units.
"""
    return explanation

# Explanation for Chi-Square Tests
def explain_chi_square(result):
    if result["type"] == "Goodness of Fit":
        observed = result["observed"]
        expected = result["expected"]
        chi_stat = result["chi_statistic"]
        p_val = result["p_value"]

        explanation = f"""
### 📐 Chi-Square Goodness of Fit Test Explanation

We use the formula:  
**χ² = Σ((Oᵢ - Eᵢ)² / Eᵢ)**

Where Oᵢ = observed frequency, Eᵢ = expected frequency

| Category | Observed (O) | Expected (E) | (O - E)² / E |
|----------|--------------|--------------|--------------|
"""

        for o, e in zip(observed, expected):
            term = ((o - e) ** 2) / e
            explanation += f"|    -     |     {o}      |     {e}      |    {term:.2f}    |\n"

        explanation += f"""  
**χ² = {chi_stat:.4f}**  
**p-value = {p_val:.4f}**

A lower p-value (typically < 0.05) means the observed distribution is significantly different from expected.
"""
        return explanation

    elif result["type"] == "Test of Independence":
        table = result["input_table"]
        expected = result["expected_freq"]
        chi_stat = result["chi_statistic"]
        p_val = result["p_value"]
        dof = result["degrees_of_freedom"]

        explanation = f"""
### 📐 Chi-Square Test of Independence Explanation

We test if two categorical variables are independent.

**χ² = Σ((Oᵢⱼ - Eᵢⱼ)² / Eᵢⱼ)** for all cells

Degrees of Freedom = (rows - 1) × (columns - 1) = **{dof}**  
**χ² = {chi_stat:.4f}**  
**p-value = {p_val:.4f}**

A small p-value (typically < 0.05) indicates that variables are not independent (i.e., they are associated).
"""
        return explanation

    else:
        return "No explanation available for the selected test."
