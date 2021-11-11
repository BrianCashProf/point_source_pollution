#dispersion
import numpy as np
from parameters import *

def dispersionx(A):
    num_particles = len(A)
    R_dispersion = np.zeros((num_particles))
    c_h = np.sqrt(2.0 * K_h /dt)
    for i in range(0,num_particles):
        if A[i] == 1:
            R_dispersion[i] = np.random.normal(0.0,c_h)
        else:
            R_dispersion[i] = 0.0

    return R_dispersion
