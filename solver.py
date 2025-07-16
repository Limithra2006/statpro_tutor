import numpy as np
from scipy import stats

# Mean, Variance, Std Dev
def solve_statistics(data):
    arr = np.array(data)
    mean = np.mean(arr)
    variance = np.var(arr)
    std_dev = np.std(arr)
    return {
        "mean": mean,
        "variance": variance,
        "std_dev": std_dev
    }

# Binomial Probability
def solve_binomial(n, p, k):
    prob = stats.binom.pmf(k, n, p)
    return {"binomial_prob": prob}

# Z-Score from sample
def solve_z_score_from_sample(values, x):
    values = np.array(values)
    mean = np.mean(values)
    std = np.std(values, ddof=1)
    z = (x - mean) / (std / np.sqrt(len(values)))
    return z

# One-sample T-test
def solve_t_test(values, pop_mean):
    values = np.array(values)
    n = len(values)
    s = np.std(values, ddof=1)
    t_stat = (np.mean(values) - pop_mean) / (s / np.sqrt(n))
    p_val = stats.t.sf(np.abs(t_stat), df=n - 1) * 2  # two-tailed test
    return t_stat, p_val

# Chi-Square - Goodness of Fit
def chi_square_goodness(observed, expected):
    observed = np.array(observed)
    expected = np.array(expected)

    # Check shape match
    if observed.shape != expected.shape:
        raise ValueError("Observed and expected must have the same shape")

    chi_stat, p_val = stats.chisquare(f_obs=observed, f_exp=expected)
    return {
        "type": "Goodness of Fit",
        "observed": observed.tolist(),
        "expected": expected.tolist(),
        "chi_statistic": chi_stat,
        "p_value": p_val
    }

# Chi-Square - Test of Independence
def chi_square_independence(table):
    table = np.array(table)

    if table.ndim != 2:
        raise ValueError("Contingency table must be 2D")

    chi_stat, p_val, dof, expected = stats.chi2_contingency(table)
    return {
        "type": "Test of Independence",
        "chi_statistic": chi_stat,
        "p_value": p_val,
        "degrees_of_freedom": dof,
        "expected_freq": expected.tolist(),
        "input_table": table.tolist()
    }
