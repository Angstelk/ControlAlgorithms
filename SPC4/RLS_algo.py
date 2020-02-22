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

U(k)- noise

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
        
        Y.append(a*Y[k-1] +b*U[k-1]+ (Z[k-1]/100))
    
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
def plot_part11(K_t,a,b, U):
   
    plt.grid(linewidth=2)
    plt.plot(K_t,U)
    plt.plot(a)
    plt.title("Odpowiedz systemu na wzbudzenie szumem")
    #plt.show();
    

def RLS(Y_old,Y_new,U_new, P, theta, alpha) :
    
    phi = np.array( ([ [Y_old] , [U_new ]] ))   
    P_old = P
    
    tmp1=np.dot(P_old,phi)
    tmp2=np.dot(tmp1,phi.transpose())
    tmp3=np.dot(tmp2,P_old)
    
    tmp4=np.dot(phi.transpose(),P_old)
    tmp5=np.dot(tmp4,phi)
    tmp5=tmp5+alpha

    P = (P_old- (tmp3/tmp5))/alpha

    
    tmp8 = np.dot(P,phi) 
    tmp9 = np.dot(phi.transpose(),theta)
    tmp10 = Y_new - tmp9
    
    tmp11 = np.dot(tmp8, tmp10)
    theta = theta + tmp11
    
    return theta,P


#Global Parametrers--------------------------------

K_t = np.linspace(0,8000,8000)
a=0.89
b=50
n = 2
P = np.eye(n,n)*1000
theta= np.array([0,0])


#PART11-----------------------------------------------------------------------------------    


Z=np.random.randn(1,len(K_t)) # noise generation
Z=np.asarray(Z)          #array transformation
Z=np.asarray(Z).squeeze()       # fitting sizes 
U=np.random.rand(len(K_t))     # Noise input 
Y=System(U,a,b,Z)             # computing system response 
    



#PART12-----------------------------------------------------------------------------------    

# initialization parameters

A=[]
B=[]

for k in range(1,len(K_t)):
    theta, P = RLS( Y[k-1], Y[k], U[k], P, theta, 1 )
print(theta)

   
    A.append(x[0])                      
    B.append(x[1])
    
    U_est.append(Opt_ster_est(k,A[k], B[k],1,Z))
 
 
"""

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





"""

