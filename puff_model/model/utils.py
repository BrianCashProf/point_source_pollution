from parameters import *
import os

def inside_chimney(R, zone=False, source='chimney'):
    if source == 'car':
        height = 0.2
        x_range = 1e-5
        y_range = 5e-5
        z_lim = (height, height+ x_range)
        x_lim = (start_lat, start_lat+ x_range)
        y_lim = (start_lon, start_lon+ y_range)
        xzin = ((R[:,0] < z_lim[1]) & (R[:, 0] > z_lim[0])
                &(R[:,1] < x_lim[1]) & (R[:, 1] > x_lim[0]))
        yin = (R[:,2] < y_lim[1]) & (R[:, 2] > y_lim[0])
        return xzin, yin, (xzin & yin)
        
    else:
        center = np.array([start_lat, start_lon])
        r = np.sum(np.square(R[:, 1:] - center), axis=1)
        #rcut = rc if not zone else 2*zone
        rcut = rc
        xyin = (r<rcut**2)
        zin = (R[:, 0] < hc)
        return xyin, zin, (xyin & zin)

def touch_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)

