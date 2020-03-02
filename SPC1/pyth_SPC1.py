import numpy as np
from scipy import signal
from numpy.polynomial import polynomial as P
import control
import matplotlib.pyplot as plt

def plot(roots,name):
                 print("roots :  ",roots)
	         mian=P.polyfromroots(roots)
        	 print(mian)
        	 sys1=control.TransferFunction(1,mian)
        	 print(sys1)
 
        	 yout2,T2=control.impulse_response(sys1)
        	 yout,T=control.step_response(sys1)
 
 
        	 fig, (ax1,ax2,ax3)=plt.subplots(nrows=3,ncols=1,figsize=(10  ,10))
        	 plt.subplots_adjust(hspace=0.80, wspace=0.20, bottom=0.11, left=0.12 , top=0.88)
        	 ax3.set_title('Step response')
         	 ax2.set_title('Impulse response')
         	 ax1.set_title('Transmittance poles')
         	 ax1.grid()
         	 ax2.grid()
        	 ax3.grid()
        	 ax3.set(xlabel='time',ylabel='val')
        	 ax1.set(xlabel='real',ylabel='img')
        	 ax2.set(xlabel='time',ylabel='val')
        	 ax3.plot(yout,T)
        	 ax2.plot(yout2,T2)
        	 for x in range(0,len(roots)):
             		ax1.plot(roots[x].real,roots[x].imag,'ro')
               	 fig.savefig(name)
                 plt.show()
s1=complex( -3, 1)
s2=complex(  -3,-1)
roots=[s1,s2]
plot(roots,'plot')


