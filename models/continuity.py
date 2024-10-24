import numpy as np

def continuity_equation_solver(n, p, G, R, dx, dt):
    """Solve the electron and hole continuity equations using finite differences."""
    dn_dt = (G - R) + np.diff(n) / dx**2  # Finite-difference approximation
    dp_dt = (G - R) + np.diff(p) / dx**2
    n_new = n + dn_dt * dt  # Euler update
    p_new = p + dp_dt * dt
    return n_new, p_new
