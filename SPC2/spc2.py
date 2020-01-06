

import numpy as np
import cmath
from scipy import signal
from numpy.polynomial import polynomial as P
import control 
from control.matlab import lsim as sim
import matplotlib.pyplot as plt
from array import array
import scipy 
from numpy import trapz 
a=10000   # jakis parametr wzmocnienia
s1=0.0001   # czynniki w mianowniuku 
s2=0.00001    # drugi czynni w mianowniku

def E(t,k,sys):
        
        sys_r=control.TransferFunction([k],[1])
        sys_tmp=1/(1+sys_r*sys)
        t, yout = control.step_response(sys_tmp,t)
        return yout,t
def E2(t,k,sys):
        
        sys_r=control.TransferFunction([k],[1])
        sys_tmp=1/(1+sys_r*sys)
        t, yout = control.step_response(sys_tmp,t)
        plt.plot(t,yout)
        plt.title("error")
        plt.show()
        Y=np.square(yout)
        plt.plot(t,Y)
        plt.title("SQRD_error")
        plt.show()
        val=trapz(Y,t)
        print(val)
        return yout,t


def Q(K,sys):
        T= np.linspace(0,100,200)
        y , t = E(T,K,sys) 
        Y=np.square(y)
        val=sum(Y)
        return val
def find_minQ(minimal,maximal,step, sys):
        
        st=array('f')
        k=array('f')
        i=minimal
        while i < maximal:
             st.append(Q(i,sys))
             k.append(i)
             i=i+step 
        min_val=min(st)   
        print("K wynosi :", st.index(min_val))
        plt.plot(k,st,'k')
        plt.title("Uchyb systemu od K")
        plt.xlabel("wartosci wzmocnienia regulatora P")
        plt.ylabel("Blad systemu")
        #plt.show()
        plt.savefig("K_wykres")
        return min_val, st.index(min_val)
def Sys_resp(Ko, Kr,t):
        Sys = control.feedback(Kr*Ko)
        T,Y = control.step_response(Sys,t)
        return T , Y
def P(K):
        K_r=control.TransferFunction([K],[1])
        return K_r


#mian = P.polyfromroots((s1,-s2))
mian=np.polynomial.polynomial.polyfromroots((-s1,-s2))

print(mian)
tmp=mian[0]                     
mian[0]=mian[2]
mian[2]=tmp
                             # szybka zamiana kolejnosci pierwiastkow w mianowniku       

K_o=control.TransferFunction([1,a],mian)    # transmitancja obiektu 
print(K_o)
T= np.linspace(0,3,200)

#min_val,K_min=find_minQ(0,800,1,K_o)

T, Y_out = Sys_resp(K_o,P(70),T)
plt.figure()
plt.plot(T,Y_out,'k')
plt.xlabel("T")
plt.ylabel("Wartosci Y")
plt.title("Odpowiedz skokowa ukladu regulacji")
plt.show()
