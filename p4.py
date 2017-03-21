#takes file containing voltage and current data (separated by comma) and plots p(t)=log v(t)*i(t) against t

import math as m
import matplotlib.pyplot as pl


#user input
fn=raw_input("Which file would you like to read from?: ")
f=open(fn,"r")

#empty lists
i=[]
v=[]
p=[]

#data read
for x in f.readlines()[3:]:
    tk = x.split(",")
    i.append(float(tk[0]))
    v.append(float(tk[1]))
f.close()

#for list refs
t=range(len(v)-1)

#calculation
for x in t:
	p.append(m.log(v[x]*i[x]))

#plot
pl.title("ln Power ")
pl.plot(t,p,'c')
pl.xlabel('Time')
pl.ylabel('p(t)')
pl.show()