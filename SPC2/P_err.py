import numpy as np
import cmath
from scipy import signal
from numpy.polynomial import polynomial as P
 
import control
from control.matlab import lsim as sim
import matplotlib.pyplot as plt
from array import array
  
a=6   # jakis parametr wzmocnienia
s1=4    # czynniki w mianowniuku 
s2=3    # drugi czynni w mianowniku

def Q(k):
        t= np.linspace(0,100,200)
        sys_err=control.TransferFunction([1,s1+s2,s1*s2],[1,s1+s2+k,k*a+s1*s2])
        T,Y=control.step_response(sys_err,t)
        Y2=np.power(Y,2)
        val=sum(Y2)
        return val

def Q_min(minimum,maximum):
        K=np.linspace(minimum,maximum,100)
        i=0
        V=[None]*len(K)
        while i < len(K):
           V[i]= Q(K[i])
           i=i+1   
        plt.plot(K,V)
        plt.show()


Q_min(-100,100)


