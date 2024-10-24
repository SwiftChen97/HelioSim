import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import spsolve
from scipy.constants import e, epsilon_0

def poisson_solver(psi, n, p, N_d, N_a, dx, epsilon_r=11.7):
    """Solve Poisson's equation in 1D."""
    epsilon = epsilon_0 * epsilon_r  # Permittivity of the material
    rho = e * (p - n + N_d - N_a)  # Charge density

    # Setup the finite-difference equation for Poisson
    A = diags([1, -2, 1], [-1, 0, 1], shape=(len(psi), len(psi))) / dx**2
    b = -rho / epsilon

    # Solve for electrostatic potential psi
    psi = spsolve(A, b)
    return psi