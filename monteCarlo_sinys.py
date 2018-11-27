# -*- coding:utf-8 -*-

import sys
sys.path.append('/usr/local/anaconda3/lib/python3.6/site-packages')

from numpy import sin,linspace

x=linspace(0,4,101)
y=sin(x/2)* sin(x/2)

from matplotlib import pyplot as plt
plt.grid()
plt.plot(x,y,'go')
plt.show()
