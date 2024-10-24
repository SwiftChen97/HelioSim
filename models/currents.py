import numpy as np
from scipy.constants import e

def current_density(n, p, E, dx, mu_n=0.14, mu_p=0.05):
    """Calculate current densities for electrons and holes using drift-diffusion model."""
    Jn = e * mu_n * (n * E + np.diff(n) / dx)  # Electron current density
    Jp = e * mu_p * (p * E - np.diff(p) / dx)  # Hole current density
    return Jn, Jp
