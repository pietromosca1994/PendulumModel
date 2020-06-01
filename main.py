from vpython import *
import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from pendulum_model import *

VISUAL_FLAG=True
theta_0=np.pi/3               # [rad] initial angle
omega_0=0               # [rad/s] initial angular speed
m=1                     # [kg] mass of the pendulum
L=1                     # [m] length of the pendulum
end_time=20             # [s] maximum time 
dt=0.01                 # [s] time increment

# external force function
def F_ext_fun(time):
    a=1                         # [N] force amplitude
    f_r=1/(2*np.pi)*sqrt(G/L)   # [Hz] pendulum resonance freuency
    f=f_r                       # [Hz] external force frequency
    return a*np.sin(2*np.pi*f*time)

# pendulum initialisation
pend=pendulum(m, L, dt)
# pendulum dynamics computation
time, theta, omega, alpha, F_ext=pend.compute_dynamics(end_time, theta_0, omega_0, F_ext_fun)

# dynamics visualisation
if VISUAL_FLAG==True:
    pend.visualize_dynamics(time, theta, F_ext)
     
fig = plt.figure()
plt.plot(time, theta, color='tab:blue')
print('max=' + str(np.max(theta)))


