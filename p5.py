#takes projectile's initial velocity, launch angle theta, normalised drag coefficient beta
#and time increment delta t to plot projectile path in 2D space
#works for speeds and angles>0 
import math as m
import matplotlib.pyplot as pl
import sys
import numpy as np


#inputs
v0=float(raw_input("Please enter initial velocity v0 (m/s): "))
th=m.radians(float(raw_input("Please enter angle theta from the horizontal of v0 (deg): "))) #deg input convert to rad
b=float(raw_input("Please enter normalised drag coefficient beta: "))
dt=float(raw_input("Please enter time step interval delta t (s): "))


#initial values
g=9.81 	#gravitational accel.

vx=v0*m.cos(th)   #velocity components
vy=v0*m.sin(th)
v=m.sqrt(vx**2+vy**2) #|v|

ax=(-b)*vx*v  
ay=(-b)*vy*v-g

x=0  #position components
y=0

xl=[0] #plot data list init
yl=[0]

#calculation of position values
def calc():

	while y>=0: #projectile cannot burrow underground
		#global variables declaration
		global ax
		global ay
		global vx
		global vy
		global v
		global x
		global y

		#acceleration components
		ax=(-b)*vx*v  
		ay=(-b)*vy*v-g
		
		#velocity components incremented
		vx+=ax*dt
		vy+=ay*dt
		v=m.sqrt(vx**2+vy**2) #|v|

		#position components incremented
		x+=dt*vx
		y+=dt*vy

		#path plot data
		xl.append(x)
		yl.append(y)	


#plot
def plt():
	pl.title("Projectile Trajectory")
	pl.plot(xl,yl,'c')
	pl.xlabel('x (m)')
	pl.ylabel('y (m)')
	pl.ylim(0)
	pl.show()


def main():
	calc()
	plt()

main()

