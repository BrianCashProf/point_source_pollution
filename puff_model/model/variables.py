#variables
import numpy as np
from parameters import *

#particle #,  location of paritcles
Rnew = np.zeros((num_particles,3)) #lat,lon,alt
Rold = np.zeros((num_particles,3)) #lat,lon,alt
R_step1 = np.zeros((num_particles,3)) #lat,lon,alt
R_step2 = np.zeros((num_particles,3)) #lat,lon,alt
R_step3 = np.zeros((num_particles,3)) #lat,lon,alt
R_step4 = np.zeros((num_particles,3)) #lat,lon,alt
Active = np.ones((num_particles)) #lat,lon,alt
