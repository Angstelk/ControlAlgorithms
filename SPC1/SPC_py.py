
import numpy as np
import cmath
from scipy import signal
from numpy.polynomial import polynomial as P
import control 
from control.matlab import lsim as sim
import matplotlib.pyplot as plt

def plot(roots,name):
	print("pierwiastki ",roots)
	mian=P.polyfromroots(roots)
	print(mian)
	a=mian[0]	
	mian[0]=mian[2]
	mian[2]=a
	#sys1=signal.TransferFunction(1,mian)
	sys1=control.TransferFunction(1,mian)
	print(sys1)

 	yout2,T2=control.impulse_response(sys1)
	yout,T=control.step_response(sys1)

	#T,yout=signal.step(sys1)
	#T2,yout2=signal.impulse2(sys1)

	fig, (ax1,ax2,ax3)=plt.subplots(nrows=3,ncols=1,figsize=(10  ,10))
	plt.subplots_adjust(hspace=0.80, wspace=0.20, bottom=0.11, left=0.12 , top=0.88)
	#plt.axes()
	ax3.set_title('Odpowiedz skokowa')
	ax2.set_title('Odpowiedz impulsowa')
	ax1.set_title('Pierwiastki ukladu')
	ax1.grid()
	ax2.grid()
	ax3.grid()
	ax3.set(xlabel='czas',ylabel='ampituda')
	ax1.set(xlabel='rzeczywiste',ylabel='urojone')
	ax2.set(xlabel='czas',ylabel='ampituda')
	ax3.plot(yout,T)
	ax2.plot(yout2,T2)
 	for x in range(0,len(roots)):
	    ax1.plot(roots[x].real,roots[x].imag,'ro')
	fig.savefig(name)

def Bode_plot(sys,name):
	phase='_phase'
	magnitude='_magnitude'
	ph_name=name+phase
	mag_name=name+magnitude
	
	w, mag, phase = signal.bode(sys)
	fig2=plt.figure()
	plt.semilogx(w,mag) #magnitude
	plt.title('Charakterystyka ampitudowa')
	plt.xlabel("pulsacja ")
	plt.ylabel("wzmocnienie")
	plt.ylim(-190,190)
	fig2.savefig(mag_name)
	plt.show()	
	
	fig3=plt.figure()
	plt.semilogx(w,phase)#phase   
	plt.title('Charakterystyka fazowa')
	plt.xlabel("pulsacja ")
	plt.ylim(-190,190)
	plt.ylabel("faza")	
	fig3.savefig(ph_name)	
	plt.show()

s11=complex(   4 , 0 )
s12=complex(   1 , 0 )

s21=complex(   1 , 0 )
s22=complex(  -4 , 0 )

s31=complex(  -1 , 0 )
s32=complex(  -2 , 0 )

s41=complex(  -1 , 0 )
s42=complex(  -40, 0 )


s51=complex(  0  , 0 )
s52=complex(  0  , 0 )

s61=complex(   0 , 0)
s62=complex(  -40, 0 )

s71=complex(  -1 , 10)
s72=complex(  -1 ,-10)

s81=complex(  -10  , -100 )
s82=complex(  -10 , 100)

s91 =complex(    2 , -30)
s92=complex(     2 , 30 )

names= ['wykres1','wykres2','wykres3','wykres4','wykres5','wykres6','wykres7','wykres8','wykres9']
roots1=[s11,s21,s31,s41,s51,s61,s71,s81,s91]
roots2=[s12,s22,s32,s42,s52,s62,s72,s82,s92]
roots=[roots1[0],roots2[0]]

#for x in range(0,len(roots1)):
#    roots=[roots1[x],roots2[x]]
#    plot(roots,names[x])


########## Cz. II u(t)= sin(wt), y(t)=A*sin(wt+fi), A=|K(jw)| fi=arg(K(jw))
########## K(s)= 3/(s+5)(s+8)
########## u(t)= sin(wt)	
w=5
sys=control.TransferFunction(3,[1,13,40])
print(sys)
WJ=3/(65j+15)
Fi=cmath.phase(WJ)
A=abs(WJ)
print(Fi, A)
#t = np.arange(0	, 10, 0.1);
#S_out =A*np.sin(w*t+Fi)
#S_in =np.sin(w*t)
#yout, T, xout =sim(sys, S_in, t)
#plt.figure()
#ax=plt.subplot(111)
#ax.plot(t,S_out, label='odpowiedz wyliczona')
#ax.plot(t,yout, label='odpowiedz symulacyjna')
#plt.xlabel("czas")
#plt.ylabel("ampituda")
#plt.title("Odpowiedz systemu")
#ax.legend(loc='upper center')
#plt.show()
#fig3.savefig("jeszcze")
############### NYQ
control.nyquist(sys,linewidth=0.25 )
plt.show()
################# BODEEEE MANUJJJ #############333

Prop = signal.lti([1],[1])
Bode_plot(Prop,"propor")
Integ= signal.lti([1],[1,0])
Bode_plot(Integ,"integ")
Diff= signal.lti([1,0],[1])
Bode_plot(Diff,"diff")
Iner=signal.lti([1],[4,1])
Bode_plot(Iner,"iner")
Osc1=signal.lti([1],[1,1,1])
Bode_plot(Osc1,"Osc") 
Osc2=signal.lti([1,1],[-1,-10,1])
Bode_plot(Osc2,"Osc2") 







