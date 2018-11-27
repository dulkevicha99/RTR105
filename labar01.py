from math import sin

def mans_sinuss(x):
    k = 1
    a = x**2/4
    S = a
    print("a1 = %6.2f S1 = %6.2f"%(a,S))

    while k <= 500:
        k = k + 1
        R = (-1)*x**2/((2*k-1)*(2*k))
        a = a * R
        S = S + a
        if k == 499:
            print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))
        if k == 500:
            print("a%d = %6.2f S%d = %6.2f"%(k,a,k,S))

    return S

print("Sin aprekinasana")
print("")

x = float(input("Ievadi argumentu (x): "))


y = sin(x/2) * sin(x/2)
print("PC sin:", y)
print("")

yy = mans_sinuss(x)
print("My sin:", yy)





print("         500")
print("         -----")
print("         \\                           k+1  2*k")
print("          \\                        (-1) * x")
print"sin(x/2)*sin(x/2)=",x,"  =>     -----------------"
print("          /                         2*(2*k)!")
print("         /")
print("         -----")
print("          k=1")




print("                              2")
print("                        (-1)*x")
print("rekurences reizinatajs:-------------")
print("                        (2*k-1)(2*k)")
