import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def conver(x):
	t=0.1
	z=(2/t)*np.tan(x/2)
	return z
a=input("enter sequence")
ws=conver(a)
print(ws)
wpb=1
b=input("enter sequence")
wp=conver(b)
print(wp)
wsb=wp/ws
ds=input("enter del s value")
dp=input("enter del p value")
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
w=np.linspace(0,np.pi,1000)
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























