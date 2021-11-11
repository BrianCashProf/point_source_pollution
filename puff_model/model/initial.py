import numpy as np
from parameters import *

def initial(sigma_lat,sigma_lon, source='chimney', n_particles=5000):
    R = np.zeros((n_particles, 3))
    if source == 'car':
        height = 0.2
        x_range = 1e-5
        y_range = 5e-5 # length of the pipe
        for i in range(0,n_particles):
            R[i,0] = height + x_range* np.random.uniform()
            R[i,1] = start_lat + x_range* np.random.uniform() 
            R[i,2] = start_lon + y_range* np.random.uniform() 
    else:
        for i in range(0,n_particles):
            R[i,0] = hc* np.random.uniform()
            R[i,1] = np.random.normal(start_lat,sigma_lat)
            R[i,2] = np.random.normal(start_lon,sigma_lon)

    return R

