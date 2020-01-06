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

class PID:
    def __init__(self,kp=0,kd=0,ki=0,ti=0,system=0,setpoint=0,dt=None):
        self.Kp=kp
        self.Kd=kd
        self.Ki=ki
        self.Ti=ti
        self.System=system
        self.SetPoint=setpoint
        self.dt=dt
    def Transs_sdm(self):
        P=control.TransferFunction(self.Kp,1,self.dt)    # Prop
        I=control.TransferFunction(self.Ki,[1,0],self.dt)  # Int
        D=control.TransferFunction(self.Kd,1,self.dt)    # Derr
        PID=P+I+D
        return PID
    def Get_P():
        return self.Kp
    def Get_I():
        return self.Ki
    def Get_D():
        return self.Kd

    def Tune(self):
        print(self.Kp,self.Kd,self.Ki,self.Ti,self.System,self.SetPoint,self.dt)    

class Control_System:
    def __init__(self,ko=0,kr=0):
        self.Ko=ko
        self.Kr=kr
        self.Ko_d=control.matlab.c2d(self.Ko,True,'zoh')
        self.Kr_d=control.matlab.c2d(self.Kr,True,'zoh')
        self.Feedback=control.feedback(self.Kr*self.Ko)
        self.Feedback_d=control.matlab.c2d(self.Kr*self.Ko,True,'zoh')

        print(self.Feedback_d) 
    def Get_PID_d(self):
        return self.Feedback_d, self.Ko_d , self.Kr_d 
    def Step_Feedback(self,t):
       T , Y = control.step_response(self.Feedback,t)
       Y_d,T_d =step(self.Feedback_d,t) 
       print(" PID :", self.Kr, " obiekt :", self.Ko, "To jest feedback :", self.Feedback)
       return T , Y ,T_d ,Y_d 
   
    def Forced_response(self,t):
       T , Y = control.forced_response(self.Feedback,t)
       
       return T , Y

    def Error_response(self,t):
       G=1/(1+self.Ko*self.Kr) 
       #print(G)
       G_d=c2d(G,True, "zoh")
       T , Y = control.step_response(G,t)
       Y_d , T_d = step(G_d,t)
       return T , Y ,T_d, Y_d

    def Experiment_system_c2d(self,T):
   
        t_step, Y_step, t_step_d, Y_step_d = self.Step_Feedback(T)
        
        t_error , Y_error , t_error_d , Y_error_d = self.Error_response(T)
        
        t_pid, Y_pid , X_out = control.forced_response(self.Kr,t_error,Y_error)
        #squezzing arrays
        t_error_d=np.asarray(t_error_d)
        Y_error_d=np.asarray(Y_error_d).squeeze()
        #end
        t_pid_d , Y_pid_d,X_out_  = control.forced_response(self.Kr_d , t_error_d , Y_error_d ) 

	fig, (ax1,ax2,ax3)=plt.subplots(nrows=3,ncols=1,figsize=(10  ,10))
	plt.subplots_adjust(hspace=0.80, wspace=0.20, bottom=0.11, left=0.12 , top=0.88)
	#plt.axes()
        ax3.set_title('Odpowiedz skokowa systemu dyskretnego ')
	ax2.set_title('Odpowiedz skokowa transmitancji uchybowej')
	ax1.set_title('Odpowiedz regulatora na uchyb')
	ax1.grid()
	ax2.grid()
	ax3.grid()
	ax3.set(xlabel='czas',ylabel='Y')
	ax1.set(xlabel='czas',ylabel='Y')
	ax2.set(xlabel='czas',ylabel='Y')
	ax3.plot(t_step_d,Y_step_d,"b" )
	ax2.plot(t_error_d,Y_error_d,"g")
        #squezzing arrays
        t_pid_d=np.asarray(t_pid_d)
        Y_pid_d=np.asarray(Y_pid_d).squeeze()
        #end
        ax1.plot(t_pid_d,Y_pid_d,"k")
        plt.show()

 	fig2, (ax1_c,ax2_c,ax3_c)=plt.subplots(nrows=3,ncols=1,figsize=(10  ,10))
	plt.subplots_adjust(hspace=0.80, wspace=0.20, bottom=0.11, left=0.12 , top=0.88)
	#plt.axes()
	ax3_c.set_title('Odpowiedz skokowa systemu  ')
	ax2_c.set_title('Odpowiedz skokowa transmitancji uchybowej')
	ax1_c.set_title('Odpowiedz regulatora na uchyb')
	ax1_c.grid()
	ax2_c.grid()
	ax3_c.grid()
	ax3_c.set(xlabel='czas',ylabel='Y')
	ax1_c.set(xlabel='czas',ylabel='Y')
	ax2_c.set(xlabel='czas',ylabel='Y')
	ax3_c.plot(t_step,Y_step,"b" )
	ax2_c.plot(t_error,Y_error,"g")
        ax1_c.plot(t_pid,Y_pid,"k")
        plt.show()
               
        
