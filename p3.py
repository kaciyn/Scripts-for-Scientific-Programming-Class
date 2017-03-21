#traces out amplitude against time for a damped simple harmonic oscillator under a range on conditions
#takes values of omega0 & gamma of damped simple harmonic oscillator
#calculates x within three boundary conditions: overdamped, critically damped, & underdamped
import matplotlib.pyplot as pl
import numpy as np
import math as m

#multiple calculations loop
repeat="y"
while repeat=="y":

	#correct user input loop
	cor="n"			
	while cor=="n":

	#user inputs
		w=float(raw_input("Please input w0: "))
		v=float(raw_input("Please input gamma: "))
		pts=int(raw_input("Please input the number of points to plot: "))

		print "w0=",w
		print "gamma= ",v
		print "Number of points to plot: ",pts

		cor=raw_input("Are these values correct? (y/n)")


	#constant & x
	a=1
	xlist=[]

	#xlim & time
	lim=5*m.pi/w
	t=np.linspace(0,lim,pts)	
	
	#t=[0,pts]
	for n in t:
		#overdamped
		if v>2*w:
			p=m.sqrt((v**2)/4-w)
			b=v/(2*p)
			x=m.exp(-v*n/2)*(a*m.cosh(p*n)+b*m.sinh(p*n))
			xlist.append(x)
			
		#crit damped
		elif v==2*w:
			b=v/2
			x=m.exp(-v*n/2)*(a+b*n)
			xlist.append(x)
			
		#underdamped
		else:
			b=v/(2*w)
			w1=m.sqrt((w**2)-((v**2)/4))
			x=m.exp(-v*n/2)*(a*m.cos(w1*n)+b*m.sin(w1*n))
			xlist.append(x)
			

	#plot
	pl.title("Damped Simple Harmonic Oscillator")
	pl.plot(t,xlist,'c')
	pl.xlim(0,lim)
	pl.xlabel('Time')
	pl.ylabel('Amplitude')
	pl.show()

	repeat=raw_input("Would you like to plot another damped oscillation graph? (y/n) ")