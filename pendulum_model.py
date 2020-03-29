import numpy as np
from vpython import *

G=9.81                  # [m/s^2] gravitational acceleration

class pendulum(object):

    def __init__(self, mass, length):
        '''
        Initialise the mass and length of the pendulum
        '''        
        self.mass=mass
        self.length=length     
  
    def compute_dynamics(self, time, theta_0, omega_0, F_ext):
        '''
        Compute dynamics of the pendulum in terms of:
            theta: angle [rad]
            omega: angular speed [rad/s]
            alpha: angular acceleration [rad/s^2]
        '''       
        # initialise system properties
        dt=time[1]-time[0]
        
        # vectors initialisation
        theta=np.empty(time.shape)
        omega=np.empty(time.shape)
        alpha=np.empty(time.shape)
        
        # boundary conditions initialisation
        theta[0]=theta_0
        omega[0]=omega_0
        alpha[0]=-G/self.length*np.sin(theta[0])-F_ext[0]     
        
        # dynamics computation
        for i in range(1, time.shape[0]):
            alpha[i]=-G/self.length*np.sin(theta[i-1])-F_ext[i]
            omega[i]=omega[i-1]+alpha[i]*dt
            theta[i]=theta[i-1]+omega[i]*dt
    
        return theta, omega, alpha

    def visualize_dynamics(self, time, theta, F_ext):
        '''
        2D visualisation of the pendulum
        '''
        dt=time[1]-time[0]

        top=sphere(pos=vector(0, 0, 0), radius=0.01)
        ball=sphere(pos=self.length*vector(np.sin(theta[0]), -np.cos(theta[0]), 0), radius=.1, color=color.blue)
        string=cylinder(pos=top.pos, axis=(ball.pos-top.pos), radius=0.01, color=color.yellow)
        force=arrow(pos=ball.pos, axis=-F_ext[0]*rotate(string.axis, radians(90), axis=vector(0,0,1))/self.length, shaftwidth=0.02)
        g=vector(0, -G, 0)
        
        for i in range(1, time.shape[0]):           
            rate(1/dt)
            #update the visual representation of the ball
            ball.pos=self.length*vector(np.sin(theta[i]), -np.cos(theta[i]), 0)
            #update the string
            string.axis=ball.pos-top.pos
            # update the force
            force.pos=ball.pos
            force.axis=-F_ext[i]*rotate(string.axis, radians(90), axis=vector(0,0,1))/self.length
            


