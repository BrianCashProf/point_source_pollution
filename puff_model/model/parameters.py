import numpy as np
#parameters

num_particles = 5000
hours = 0.2 # hours
dt = 3
time_steps = int(hours * 3600. / dt) + 1

D_log = np.zeros((num_particles))
for i in range(0,num_particles):
    D_log[i] = np.random.normal(-5.0,2.5)
D = 10. ** (D_log)

#K_h = 2.0 * (10. **4.) # original volcano
#K_v = 10.

K_h = 4e-3 # car waste
K_v = 1e-4 # car waste

#K_h = 1 # current working value for the chimney
#K_v = 15 # current working value for the chimney


start_lat = 15.141667
start_lon = 120.35

sigma_lon = .0001
sigma_lat = .0001

U = np.load('u_wind.npy')
V = np.load('v_wind.npy')
W = np.load('w_wind.npy')

alt_coor = np.linspace(0,29000,30)
lat_coor = np.linspace(-90.,90.,73)
lon_coor = np.linspace(0.,360.,144)

# chimney
rc = 0.0003
hc = 420




