from vpython import *
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from pendulum_model import *

VISUAL_FLAG=False
theta_0=0               # [rad] initial angle
omega_0=0               # [rad/s] initial angular speed
m=1                     # [kg] mass of the pendulum
L=1                     # [m] length of the pendulum
time_limit=10           # [s] maximum time 
dt=0.01                 # [s] time increment
a=1                     # [N] force amplitude
f_r=1/(2*pi)*sqrt(G/L)  # [Hz] pendulum resonance freuency 
f=f_r                   # [Hz] external force frequency

# array initialisation
time=np.arange(0, time_limit, dt)
F_ext=a*np.sin(2*pi*f*time)

pend=pendulum(m, L)
theta, omega, alpha=pend.compute_dynamics(time, theta_0, omega_0, F_ext)
if VISUAL_FLAG==True:
    pend.visualize_dynamics(time, theta, F_ext)
        
fig = plt.figure()
plt.plot(theta, color='tab:blue')
print('max=' + str(np.max(theta)))


