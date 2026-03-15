import numpy as np
import matplotlib.pyplot as plt


def generate_multiple_langevin(n_traj, n_steps, dt, D):

    x = np.zeros((n_traj, n_steps))

    scale_factor = np.sqrt(2 * D * dt)

    random_kicks = np.random.normal(0.0, 1.0, size=(n_traj, n_steps))

    for traj in range(n_traj):
        for i in range(1, n_steps):
            x[traj, i] = x[traj, i-1] + scale_factor * random_kicks[traj, i-1]

    return x



def calculate_tamsd_multiple(trajectories, dt):

    n_traj, N = trajectories.shape

    max_lag = N // 2

    lags = np.arange(1, max_lag + 1) * dt

    tamsd_all = np.zeros((n_traj, max_lag))


    for traj in range(n_traj):

        x = trajectories[traj]

        for n in range(1, max_lag + 1):

            dx = x[n:] - x[:-n]

            tamsd_all[traj, n-1] = np.mean(dx**2)


    return lags, tamsd_all




# Parameters
n_traj = 5
n_steps = 5000
dt = 0.001
D = 0.5


# Generate trajectories
trajectories = generate_multiple_langevin(n_traj, n_steps, dt, D)


# Calculate TAMSD
lags, tamsd_all = calculate_tamsd_multiple(trajectories, dt)



# Plot trajectories
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)

for traj in range(n_traj):
    plt.plot(trajectories[traj])

plt.title("Multiple trajectories")
plt.xlabel("time step")
plt.ylabel("x")



# Plot TAMSD (ONLY individual TAMSD)
plt.subplot(1,2,2)

for traj in range(n_traj):

    plt.loglog(lags, tamsd_all[traj],
               linewidth=2,
               label=f"TAMSD traj {traj}")



plt.title("TAMSD (individual trajectories only)")

plt.xlabel("Lag")

plt.ylabel("TAMSD")

plt.legend()

plt.tight_layout()

plt.show()
