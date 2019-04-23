import numpy as np
import matplotlib.pyplot as plt
import cmath as cm
def conver(x):
	t=0.1
	z=(2/t)*np.tan(x/2)
	return z
a=input("enter sequence")
wp=conver(a)
print(wp)
b=input("enter sequence")
ws=conver(b)
print(ws)
ds=input("enter del s value")
dp=input("enter del p value")
e=np.sqrt(dp**(-2)-1)
k=np.sqrt(ds**(-2)-1)
k0=np.sqrt(dp**(-2)-1)
k1=k/k0
k3=np.arccosh(k1)
k4=np.arccosh(ws/wp)
N=np.ceil(k3/k4)
print("the value of n is ",N)
yn0=(np.sqrt(1+(1/(e**2))))+(1/e)
yn1=(yn0)**(1/N)
yn2=(yn0)**((-1)/N)
yn=(.5)*(yn1-yn2)
print("the value of  yn",yn)
c0=yn
k=N/2
bk1=np.sin(((2*k-1)*(np.pi))/(2*N))
bk=2*yn*bk1
l2=((2*k-1)*np.pi)/(2*N)
ck=yn**2+((np.cos(l2))**2)
print("the value of ck",ck)
print("the value of bk",bk)
w=np.arange(0,np.pi,0.01)
j=cm.sqrt(-1)
z=np.exp(j*w)
s=20*((z-1)/(z+1))
l3=(np.sqrt(1+((e)**2)))
l4=l3*(wp**2)*ck
l5=((s**2)+(bk*wp*s)+(((wp)**2)*ck))
hw=abs(l4/l5)
plt.plot(hw)
plt.show()


























