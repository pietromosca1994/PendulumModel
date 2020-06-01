import numpy as np
from vpython import *

G=9.81                  # [m/s^2] gravitational acceleration

class pendulum(object):

    def __init__(self, mass, length, dt):
        '''
        Initialise the mass and length of the pendulum
        '''        
        self.mass=mass
        self.length=length 
        self.dt=dt
    
    def initialisation(self, theta_0, omega_0, F_ext):
        '''
        boundary conditions initialisation
        '''
        theta=theta_0
        omega=omega_0
        alpha=-G/self.length*np.sin(theta)-F_ext
             
        previous_state={'theta': theta, 
                        'omega': omega, 
                        'alpha': alpha}    
        
        return previous_state
    
    
    def step(self, previous_state, F_ext):
        '''
        compute next dynamics step
        '''
        
        previous_theta=previous_state['theta'];
        previous_omega=previous_state['omega'];
        previous_alpha=previous_state['alpha'];   
        
        alpha=-G/self.length*np.sin(previous_theta)-F_ext
        omega=previous_omega+alpha*self.dt
        theta=previous_theta+omega*self.dt
        
        state={'theta': theta,
               'omega': omega,
               'alpha': alpha}
        
        return state
        
    def compute_dynamics(self, end_time, theta_0, omega_0, F_ext_fun):
        '''
        Compute dynamics of the pendulum in terms of:
            theta: angle [rad]
            omega: angular speed [rad/s]
            alpha: angular acceleration [rad/s^2]
        '''                
        # vectors initialisation
        time=[]
        theta=[]
        omega=[]
        alpha=[]
        F_ext=[]
         
        # dynamics computation
        time.append(0)
        F_ext.append(F_ext_fun(time[-1]))        
        previous_state=self.initialisation(theta_0, omega_0, F_ext[-1])
        theta.append(previous_state['theta'])
        omega.append(previous_state['omega'])
        alpha.append(previous_state['alpha'])

        
        while time[-1]<end_time:            
            time.append(time[-1]+self.dt)
            F_ext.append(F_ext_fun(time[-1]))  
            previous_state=self.step(previous_state, F_ext[-1])
            theta.append(previous_state['theta'])
            omega.append(previous_state['omega'])
            alpha.append(previous_state['alpha'])           
        
        # list to numpy array conversion
        time=np.array(time)
        theta=np.array(theta)
        omega=np.array(omega)
        alpha=np.array(alpha)
        F_ext=np.array(F_ext)
                    
        return time, theta, omega, alpha, F_ext

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
            


