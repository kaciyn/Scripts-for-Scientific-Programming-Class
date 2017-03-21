#modified version of p5; takes projectile's initial velocity, normalised drag coefficient beta
#and time increment delta t to plot the ratio of final kinetic energy 
#to initial kinetic energy against launch angle theta in range 0-90 deg
import math as m
import matplotlib.pyplot as pl
import sys



#inputs
v0=float(raw_input("Please enter initial velocity v0 (m/s): "))
b=float(raw_input("Please enter normalised drag coefficient beta: "))
dt=float(raw_input("Please enter time step interval delta t (s): "))


#initial values
g=9.81 	#gravitational accel.
thl=range(0,90,1) #angle limits
th=[] #rad init

#plot data list init
krl=[] #kf/ki

#v components init
vxl=[]
vyl=[]
y=0 #y position init
vfl=[] #vf list init


#deg to rad conversion
def rad():
	for x in thl:
		r=m.radians(x)
		th.append(r)


#calculation of final velocity values for each launch angle
def calc():

	for a in th:
		vx=v0*m.cos(a)   #velocity components
		vy=v0*m.sin(a)
		#print 'vx:',vx
		v=m.sqrt(vx**2+vy**2) #|v|
		#print 'v:',v
		ax=(-b)*vx*v   #acceleration components
		ay=(-b)*vy*v-g

		vxl.append(vx)
		vyl.append(vy)

		y=0

		while y>=0: #projectile cannot burrow underground

			#global variables declaration
			global ax
			global ay
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
			#print 'v:',v
			#position components incremented
			y+=dt*vy
			
		vfl.append(v) #vf list
		#print 'vfl:',vfl
		


def ke():
	for v in vfl:
		kr=(v**2)/(v0**2)	#ratio of Kf/Ki=.5mv0^2/.5mvf^2=v0^2/vf^2
		krl.append(kr)

#plot
def plt():
	pl.title("Projectile Ratio of final & initial kinetic energy v Launch angle")
	pl.plot(thl,krl,'c')
	pl.ylabel('Kf/Ki')
	pl.xlabel('Launch Angle Theta (deg)')

	pl.xlim(0)
	pl.show()


def main():
	rad()
	calc()
	ke()
	plt()

main()

