# -*- coding:utf-8 -*-
from math import sin

#(1.) * (2.) =(2.)- float *int =float
#(1.) * (2.) =(2.)- float * float =float#float(input()) -> float
x=1. * input ('Lietotāj,lūdzu, ievadi argumentu(x)//D.A no -bezg. līdz +bezg. :')
#print type(x)

y=(sin(x/2))**2
print "(sin(x/2))**2(%.2f) = %.2f"%(x,y)

a0 = (-1)*x**2/(2)
S0 = a0
print "a0 = %.2f SO = %.2f"%(a0,S0)

a1 = (-1)**2*x/(4)
S1 = a0 + a1
print "a1 = %.2f S1 = %.2f"%(a1,S1)

a2 = (-1)**3*x**0/(48)
S2 = a0 + a1 + a2
print "a2 = %.2f S2 = %.2f"%(a2,S2)

a3 = (-1)**4*x**(-1)/(1440)
S3 = a0 + a1 + a2 + a3
print "a3 = %.2f S3 = %.2f"%(a3,S3)

