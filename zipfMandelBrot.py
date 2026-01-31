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

# --- Example Demonstration --