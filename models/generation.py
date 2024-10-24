import numpy as np

def generation_rate(I0, alpha, x):
    """Optical generation rate based on absorption and light intensity."""
    return I0 * np.exp(-alpha * x)
