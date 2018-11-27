import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sin, linspace

x=linspace(0, 7, 70)
y=sin(x/2)*sin(x/2)
y1=x
y2=y1-x**3/(1*2*3)
y3=y2-x**5/(1*2*3*4*5)
y4=y3-x**7/(1*2*3*4*5*6*7)

from matplotlib import pyplot as plt


plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Funkcija$ sin(x/2)*sin(x/2)$')
plt.plot(x,y,color='#FF0098')
plt.plot(x,y1,color='#00FF11')
plt.plot(x,y2,color='#0000FF')
plt.plot(x,y3,color='#FFFF00')
plt.plot(x,y4,color='#00FFFF')

plt.legend(['sin(x/2)*sin(x/2)', 'x','x-x**3/(1*2*3)','x-x**5/(1*2*3*4*5)','x-x**7/(1*2*3*4*5*6*7)'], loc=3)
plt.show()

#print(plt.legend.__doc__)
