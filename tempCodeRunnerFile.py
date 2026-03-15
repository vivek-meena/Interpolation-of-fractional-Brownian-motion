import numpy as np
import matplotlib.pyplot as plt

def generate_multiple_langevin(n_traj, n_steps, dt, D):

    # Create 2D array: rows = trajectories, columns = time
    x = np.zeros((n_traj, n_steps))

    scale_factor = np.sqrt(2 * D * dt)

    # Generate all random kicks at once
    random_kicks = np.random.normal(0.0, 1.0, size=(n_traj, n_steps))

    # Update positions
    for traj in range(n_traj):
        for i in range(1, n_steps):
            dx = scale_factor * random_kicks[traj, i-1]
            x[traj, i] = x[traj, i-1] + dx

    return x


# -----------------------------
# Parameters
# -----------------------------

n_traj = 5      # number of trajectories
n_steps = 1000  # time points
dt = 0.0001
D = 0.5


# Generate trajectories
trajectories = generate_multiple_langevin(n_traj, n_steps, dt, D)


# -----------------------------
# Visualization
# -----------------------------

plt.figure(figsize=(10,6))

for traj in range(n_traj):
    plt.plot(trajectories[traj], label=f"Trajectory {traj}")

plt.title("Multiple 1D Brownian Trajectories")
plt.xlabel("Time step")
plt.ylabel("Position")
plt.legend()
plt.show()
