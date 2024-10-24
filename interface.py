import tkinter as tk
from tkinter import messagebox
from main import solar_cell_simulation

def run_simulation():
    try:
        dx = float(dx_entry.get())
        dt = float(dt_entry.get())
        max_time = float(time_entry.get())

        layers = [{'epsilon_r': 11.7, 'mu_n': 0.14, 'mu_p': 0.05, 'N_d': 1e24, 'N_a': 0}]
        psi, n, p, Jn, Jp = solar_cell_simulation(layers, dx=dx, dt=dt, max_time=max_time)

        result_message = f"Psi = {psi[:5]}\nn = {n[:5]}\np = {p[:5]}\nJn = {Jn[:5]}\nJp = {Jp[:5]}"
        messagebox.showinfo("Simulation Results", result_message)

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input or simulation error: {e}")

# Set up the GUI
root = tk.Tk()
root.title("Solar Cell Simulation")

tk.Label(root, text="dx (Spatial resolution in meters):").grid(row=0)
dx_entry = tk.Entry(root)
dx_entry.grid(row=0, column=1)

tk.Label(root, text="dt (Time step in seconds):").grid(row=1)
dt_entry = tk.Entry(root)
dt_entry.grid(row=1, column=1)

tk.Label(root, text="Max simulation time (seconds):").grid(row=2)
time_entry = tk.Entry(root)
time_entry.grid(row=2, column=1)

tk.Button(root, text="Run Simulation", command=run_simulation).grid(row=3, column=1)

root.mainloop()
