'''Useful functions shared by agents and/or AMS

'''
import numpy as np

def _rnd_vector(n_dim, magnitude=1.0):
    '''Generate random vector of specific dimension and magnitude'''

    vals = [np.random.ranf() - 0.5 for k in range(n_dim)]
    radial_adjust = np.sqrt(np.dot(vals, vals)) / magnitude

    return np.divide(vals, radial_adjust)
