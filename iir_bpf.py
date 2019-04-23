import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
#def conver(x):
#	t=0.1
#	z=(2/t)*np.tan(x/2)
#	return z
wp1=400*np.pi
wp2=1200*np.pi
ws1=160*np.pi
ws2=3000*np.pi
wpo=wp1*wp2
ws0=ws1*ws2
ds=
dp=
q=0.1*ds
p=0.1*dp
d=np.sqrt(((10**q)-1)/(10**(p)-1))
m=np.log(d)
y=(wsb/wpb)
n=np.log(y)
N=np.ceil((m/n))
print(N)
g=(.1**-2)
k=g-1
#print(g)
h=(1/(2*N))
#print(h)
i=(k**h)
#print(i)
wc=wsb/i
print(wc)
w=np.linspace(-np.pi,np.pi,1000)
j=cm.sqrt(-1)
z=np.exp(j*w)
#t=input("enter time period")
s=(20)*((z-1)/(z+1))
sb=wp/s
k1=N/2
bk=2*np.sin(((2*k1-1)*np.pi)/(2*N))
print(bk)
hw=abs((wc**2)/((sb**2)+(bk*wc*sb)+(wc**2)))
print(hw)
plt.plot(w,hw)
plt.show()























