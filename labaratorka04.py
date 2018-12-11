import sys
sys.path.append("/user/local/anaconda3/lib/python3.6/site-packages")

from numpy import random,sqrt, sin
#from math import sqrt
#from math import sin

N = 7000
N1=0

x= random.uniform(0,5,N)
y= random.uniform(0,5,N)

funct=(sin(x)*sin(x))/2

from matplotlib import pyplot as plt
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija $(sin(x)*sin(x))/2$')
plt.plot(x,funct,'o', color = "#990000")
for i in range(N):
    #plt.plot(x[i],y[i],"ko")
    if x[i] > 0 and x[i] <5:
        if y[i] >0 and y[i]< funct[i]:
            plt.plot(x[i],y[i],"go")
            N1=N1+1
        else:
            plt.plot(x[i],y[i],"ro")
plt.show()

s_zin = 5 * 5
s_nez = 1.* s_zin * N1/N
print(s_zin)
print(s_nez)
