#takes projectile's initial velocity, launch angle theta, normalised drag coefficient beta
#and time increment delta t to plot projectile path in 2-d space
import math as m
import matplotlib.pyplot as pl
import numpy as np
import sys


#inputs
v0=float(raw_input("Please enter initial velocity v0 (m/s): "))
th=m.radians(float(raw_input("Please enter angle theta from the horizontal of v0 (deg): "))) #deg input convert to rad
b=float(raw_input("Please enter normalised drag coefficient beta: "))
dt=float(raw_input("Please enter time step interval delta t (s): "))


#initial values
g=9.81 	#gravitational accel.
mx=2**25 	#arbitrarily high max time

vx=v0*m.cos(th)   #velocity components
vy=v0*m.sin(th)
v=m.sqrt(vx**2+vy**2) #|v|

ax=(-b)*vx**2   #acceleration components
ay=(-b)*vy**2-g

x=0  #position components
y=0

xl=[0] #plot data list init
yl=[0]


#v components init
vl=[]
vxl=[]
vyl=[]
y=0 #y position init
vfl=[] #vf list init

def calc():

	time=np.arange(0,mx,dt) #time range list

	for t in time:
			if y>=0: #projectile cannot burrow underground

				#global variables declaration
				global ax
				global ay
				global v
				global x
				global y
				global vl
				global vx
				global vy

				#acceleration components
				ax=(-b)*vx**2  
				ay=(-b)*vy**2-g
				
				#velocity components incremented
				vx+=ax*dt
				vy+=ay*dt
				v=m.sqrt(vx**2+vy**2) #|v|
				print 'v:',v
				#position components incremented
				y+=dt*vy
				vl.append(v) #list of velocity values
				print vl
			else: #again, projectile cannot burrow underground
				break


def plt():
	pl.title("Projectile Trajectory")
	pl.plot(xl,yl,'c')
	pl.xlabel('x (m)')
	pl.ylabel('y (m)')
	pl.ylim(0)
	pl.show()


def main():
	calc()
	#plt()

main()

