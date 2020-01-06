import time 
import numpy as np
import cmath
from scipy import signal
from numpy.polynomial import polynomial as P 
from control import *
from control.matlab import c2d
from control.matlab import *
import control 
from control.matlab import lsim as sim
import matplotlib.pyplot as plt
from array import array
import scipy 
from numpy import trapz 

class RLS:
    def __init__(self, delta=1000,p=1,Y):
        self.P=np.identity(p+1) *delta
        self.W
        self.err
        self.g
        self.
        self.

        
 
