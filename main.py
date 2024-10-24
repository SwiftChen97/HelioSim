from models.poisson import poisson_solver
from models.continuity import continuity_equation_solver
from models.currents import current_density
from models.recombination import recombination_rate
from models.generation import generation_rate
import numpy as np

def solar_cell_simulation(layers, dx=1e-9, dt=1e-12, max_time=1e-9):
    num_points = len(layers)
    psi = np.zeros(num_points)
    n = np.zeros(num_points)
    p = np.zeros(num_points)
    N_d = np.zeros(num_points)
    N_a = np.zeros(num_points)

    time = 0
    while time < max_time:
        E = -np.gradient(psi, dx)
        psi = poisson_solver(psi, n, p, N_d, N_a, dx)
        G = generation_rate(I0=1e21, alpha=1e5, x=np.linspace(0, num_points*dx, num_points))
        R = recombination_rate(n, p, n0=1e10, p0=1e10, tau_n=1e-9, tau_p=1e-9, ni=1e10)
        n, p = continuity_equation_solver(n, p, G, R, dx, dt)
        time += dt

    Jn, Jp = current_density(n, p, E, dx)
    return psi, n, p, Jn, Jp

if __name__ == "__main__":
    layers = [{'epsilon_r': 11.7, 'mu_n': 0.14, 'mu_p': 0.05, 'N_d': 1e24, 'N_a': 0}]
    psi, n, p, Jn, Jp = solar_cell_simulation(layers)
    print("Results:", psi[:5], n[:5], p[:5], Jn[:5], Jp[:5])
