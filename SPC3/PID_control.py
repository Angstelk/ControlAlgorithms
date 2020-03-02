import numpy as np
from scipy import signal
from numpy.polynomial import polynomial as P 
from PID import PID
from PID import Control_System
from control.matlab import lsim as sim
import matplotlib.pyplot as plt
import control
from control import *
from control.matlab import *


#transmitancja obiektu b/(T1s + 1)(T2s+1)(s)
b=1
T1=70
T2=7

s0=0
s1=pow(T1,-1)
s2=pow(T2,-1)
mian=P.polyfromroots([s0,-s1,-s2])

K_o=control.TransferFunction([b],mian)
#print(K_o)
print("main To jest K_o ", K_o)
#pid = PID(3,100,3,90,K_o)
pid = PID(900000,-100,3,90,K_o)
ctr=pid.Transs_sdm()
print("main To jest PID", ctr)
#pid.Tune()
Ctrl=Control_System(K_o,pid.Transs_sdm()) 
T= np.linspace(0,0.5,200)
Ctrl.Experiment_system_c2d(T)    
F,O,R=Ctrl.Get_PID_d()

print("_____________________________________________________")
print(O)
print(R)
print("_____________________________________________________")

