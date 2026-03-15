import numpy as np
import matplotlib.pyplot as plt


# -----------------------------
# Generate trajectories
# -----------------------------

def generate_multiple_langevin(n_traj,n_steps,dt,D):

    x=np.zeros((n_traj,n_steps))

    scale=np.sqrt(2*D*dt)

    noise=np.random.normal(0,1,(n_traj,n_steps))

    for traj in range(n_traj):

        for i in range(1,n_steps):

            x[traj,i]=x[traj,i-1]+scale*noise[traj,i-1]

    return x


# -----------------------------
# TAMSD
# -----------------------------

def calculate_tamsd(trajectories,dt):

    n_traj,N=trajectories.shape

    max_lag=N//2

    lags=np.arange(1,max_lag+1)*dt

    tamsd_all=np.zeros((n_traj,max_lag))

    for traj in range(n_traj):

        x=trajectories[traj]

        for n in range(1,max_lag+1):

            dx=x[n:]-x[:-n]

            tamsd_all[traj,n-1]=np.mean(dx**2)

    tamsd_mean=np.mean(tamsd_all,axis=0)

    return lags,tamsd_all,tamsd_mean


# -----------------------------
# EAMSD
# -----------------------------

def calculate_eamsd(trajectories):

    eamsd=np.mean((trajectories-trajectories[:,0][:,None])**2,axis=0)

    return eamsd


# -----------------------------
# Least square fitting
# -----------------------------

def least_square(time,msd):

    x=np.log10(time)

    y=np.log10(msd)

    m,c=np.polyfit(x,y,1)

    y_fit=m*x+c

    error=y-y_fit

    rmse=np.sqrt(np.mean(error**2))

    return m,c,y_fit,error,rmse



# PARAMETERS

n_traj=50

n_steps=5000

dt=0.001

D=0.5


# SIMULATION

trajectories=generate_multiple_langevin(n_traj,n_steps,dt,D)

lags,tamsd_all,tamsd_mean=calculate_tamsd(trajectories,dt)

time=np.arange(n_steps)*dt

eamsd=calculate_eamsd(trajectories)


# FITTING

m,c,y_fit,error,rmse=least_square(time[1:],eamsd[1:])


print("Slope =",m)

print("Diffusion coefficient =",10**c/2)

print("RMSE =",rmse)



# -----------------------------
# PLOTS
# -----------------------------

plt.figure(figsize=(14,10))


# -----------------------------------------
# SECTION 1 : TRAJECTORIES
# -----------------------------------------

plt.subplot(2,2,1)

for traj in range(5):

    plt.plot(time,trajectories[traj])

plt.xlabel("Time (seconds)  [Linear scale]")

plt.ylabel("Position x(t)  (micrometer)  [Linear scale]")

plt.title("Section 1: Brownian Trajectories")

plt.grid(True)



# -----------------------------------------
# SECTION 2 : TAMSD
# -----------------------------------------

plt.subplot(2,2,2)

for traj in range(5):

    plt.loglog(lags,tamsd_all[traj])

plt.loglog(lags,tamsd_mean,'k',linewidth=3,label="Ensemble-avg TAMSD")

plt.xlabel("Lag time Δ (seconds)  [log10 scale]")

plt.ylabel("TAMSD  (micrometer²)  [log10 scale]")

plt.title("Section 2: TAMSD")

plt.legend()

plt.grid(True)



# -----------------------------------------
# SECTION 3 : EAMSD + FIT
# -----------------------------------------

plt.subplot(2,2,3)

plt.loglog(time[1:],eamsd[1:],'b',label="EAMSD")

plt.loglog(time[1:],10**y_fit,'r--',label="Least-square fit")

plt.xlabel("Time (seconds)  [log10 scale]")

plt.ylabel("EAMSD  (micrometer²)  [log10 scale]")

plt.title("Section 3: EAMSD and Linear Fit")

plt.legend()

plt.grid(True)



# -----------------------------------------
# SECTION 4 : FITTING ERROR
# -----------------------------------------

plt.subplot(2,2,4)

plt.plot(time[1:],error)

plt.xlabel("Time (seconds)  [Linear scale]")

plt.ylabel("Error = log(MSD) − Fit  [Linear scale]")

plt.title("Section 4: Least-square fitting error")

plt.grid(True)



plt.tight_layout()

plt.show()
