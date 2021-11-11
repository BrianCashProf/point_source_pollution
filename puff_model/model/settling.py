#settling
import numpy as np
from parameters import *
R_settling = np.zeros((num_particles))
# constant = 1.09 * (10. ** 9.)
constant = 0.0

def settling(D,A):
    for i in range(0,num_particles):
        if A[i] == 1:
            R_settling[i] = 2.0 / 9.0 * constant * (D[i] ** 2.0)
        else:
            R_settling[i] = 0.0
    return R_settling
