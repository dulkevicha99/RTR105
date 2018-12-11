#Aptuveni novērojot funkcijas saknes vertību lietojot "pēli" iegūstam x=

from math import sin,fabs
from time import sleep

def f(x):
    return sin(x/2)*sin(x/2)
k=0
a= -1
b=1

funa =f(a)
funb =f(b)

if (funa*funb >0.0):
    print('Dotāja intervala[%s,%s] sakņu nav'%(a,b))
    sleep(1);exit()
else:
    print('Dotāja intervala sakne(s) ir!')
deltax= 0.0001

while(fabs(b-a)> deltax):
    k=k+1
    x=(a+b)/2.;funx=f(x)
    if(funa*funx<0.):
        b=x
    else:
        a=x


print('Sakne ir: ',x)
print('Sakne ir: ',f(x))
print('Interaciju skaits k= ',k)
