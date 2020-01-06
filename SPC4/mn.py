import numpy as np
import cmath
from scipy import signal
from numpy.polynomial import polynomial as P 
import control 
from control.matlab import lsim as sim
import matplotlib.pyplot as plt
from control import *
from control.matlab import *
from array import array

"""
1)
                                SYSTEM
*-------------------------------------------------------------*
*                                                             *
*                           U  _____     | Z     Y            *   
*                        ---->|_____|--->o-------->           *
*                                        +                    *
*-------------------------------------------------------------*

U(k)- step

Y_k= a*Y_(k-1)+b*U_(k)+Z_u(k)

Z_k ~N(0,sig^2)

"""
def Step(x): 
    U=np.ones(x)
    U[0]=0
    U[1]=0.5
    return U 

def System(U,a,b,Z):
    Y=[]
    Y.append(0)

    for k in range(1,len(U)):
        
        #Y.append(a*Y[k-1] +b*U[k-1])
        Y.append(a*Y[k-1] +b*U[k-1]+Z[k-1])
    
    return Y;

def System_lin(a,b,Z):
    Y=[]
    Y.append(0)

    for k in range(1,len(U)):
        
        Y.append(a*k +b*+Z[k-1])
    
    return Y;
def Opt_ster(K,a,b,Y,Z):
    U=[]
    for k in range(len(K)):
        U.append((Y-a-Z[k])/b)
    return U

def Opt_ster_est(k,a_es,b_es,Y,Z):
    U=((Y-a_es-Z[k])/b_es)
    return U

#CZ1-----------------------------------------------------------------------------------    
K_t = np.linspace(0,1999,2000)
Z=np.random.randn(1,len(K_t))*0.5
Z=np.asarray(Z)
Z=np.asarray(Z).squeeze()
step=Step(len(K_t))
U=np.random.rand(len(K_t))
Y=System(U,0.5,1,Z)
Y=System_lin(0.7,20,Z)

#plt.plot(K_t,U)
#plt.plot(K_t,Y)
#plt.show()




#CZ2-----------------------------------------------------------------------------------    

def rlse_online(aT_k1,b_k1,x,P,alpha): # pierwszy argument to [zmienna niezalezna: 1] drugi argument to Y od iteratora do konca , trzeci 

    K = np.dot(P,aT_k1.T)/(np.dot(np.dot(aT_k1,P),aT_k1.T)+1)
    x = x +K*(b_k1-np.dot(aT_k1,x))
    P = (P-np.dot(K,np.dot(aT_k1,P)))
    return x,K,P


Ya=np.array([Y]).T

n = 2
vals = np.array([[0.0,1.0,2.0,3.0,4.0,5.0,6.0,7.0]]).T
P = np.eye(n,n)*1000.
x = np.zeros((n,1))

Y_lin=[]

A=[]
B=[]
U_est=[]
a=0.5
b=10

for i in range(len(K_t)):
    Y_lin.append(i)
    Y_lina=np.array(Y_lin)


for k in range(len(K_t)):
    x,K,P = rlse_online(np.array([[K_t[k],1]]),Ya[k,:],x,P,0.5)
    
    #a_est=x[0]
    #b_est=x[1]
    
    A.append(x[0])
    B.append(x[1])
    
    U_est.append(Opt_ster_est(k,A[k], B[k],1,Z))


np.
plt.grid(linewidth=2)
plt.plot(K_t,A)
plt.plot(a)
plt.title("A")
plt.show();

plt.grid(linewidth=2)
plt.plot(K_t,B)
plt.plot(b)
plt.title("B")
plt.show();


U=Opt_ster(K_t,a,b,1,Z)
plt.grid(linewidth=2)
plt.plot(K_t,U)
plt.show();

plt.grid(linewidth=2)
plt.plot(K_t,U_est)
plt.show();




