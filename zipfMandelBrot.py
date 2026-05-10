import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def zipf_mandelbrot_law(r, C, alpha, beta):
    """
    The Zipf-Mandelbrot Law function: f(r) = C / (r + beta)^alpha
    """
    return C / ((r + beta) ** alpha)

def fit_zipf_mandelbrot(ranks, frequencies):
    """
    Fits the Zipf-Mandelbrot Law to frequency data using non-linear least squares.
    """
    # Initial guesses for [C, alpha, beta]
    # C is often roughly the frequency of rank 1
    # alpha is usually around 1.0
    # beta is usually small (e.g., 1.0 - 5.0)
    initial_guess = [frequencies[0], 1.0, 2.0]
    
    # Define bounds to keep parameters physically meaningful
    # C > 0, alpha > 0, beta >= 0
    bounds = (0, [np.inf, 5.0, 100.0])

    params, covariance = curve_fit(
        zipf_mandelbrot_law, 
        ranks, 
        frequencies, 
        p0=initial_guess,
        bounds=bounds
    )
    
    return params

# --- Example Demonstration ---

# 1. Create Mock Data (Zipf-Mandelbrot with some noise)
true_C, true_alpha, true_beta = 5000, 1.1, 2.5
ranks = np.arange(1, 101)
pure_frequencies = zipf_mandelbrot_law(ranks, true_C, true_alpha, true_beta)
noise = np.random.normal(0, 0.05 * pure_frequencies) # 5% noise
observed_frequencies = np.abs(pure_frequencies + noise)

# 2. Perform the fit
C_fit, alpha_fit, beta_fit = fit_zipf_mandelbrot(ranks, observed_frequencies)

# 3. Generate fitted curve for plotting
fitted_frequencies = zipf_mandelbrot_law(ranks, C_fit, alpha_fit, beta_fit)

# 4. Visualization
plt.figure(figsize=(12, 6))

# Plot 1: Linear Scale
plt.subplot(1, 2, 1)
plt.scatter(ranks, observed_frequencies, s=10, label='Observed Data', alpha=0.6)
plt.plot(ranks, fitted_frequencies, color='red', label='Mandelbrot Fit')
plt.title("Linear Scale Fit")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.legend()

# Plot 2: Log-Log Scale (where the curve at the head is visible)
plt.subplot(1, 2, 2)
plt.loglog(ranks, observed_frequencies, 'o', markersize=4, label='Observed Data', alpha=0.6)
plt.loglog(ranks, fitted_frequencies, color='red', label='Mandelbrot Fit')
plt.title("Log-Log Scale Fit")
plt.xlabel("Log(Rank)")
plt.ylabel("Log(Frequency)")
plt.legend()

plt.tight_layout()
plt.show()

print(f"--- Fit Results ---")
print(f"Constant (C): {C_fit:.2f}")
print(f"Exponent (alpha): {alpha_fit:.2f}")
print(f"Shift (beta): {beta_fit:.2f}")