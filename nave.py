import math as mt

c=3e8  #m/s
x=input("estime la distancia en años luz x:")
x=float(x)

v=input("estime la velocidad en fraccion de c:")
v=float(v)
ly=9.461e15 #m
dis=x*ly  #sg 
tiempo=dis/v #s
fac=mt.sqrt(1-((v**2)/(c**2)))
t=(ly-((v*x)/(c*c)))/fac
print("el tiempo que tarda nave en llegar al plane visto desde la tierra es:")
print(t)
print("el tiempo que tarda nave en llegar al plane visto desde la tierra es:")
print(tiempo)

print("EJERCICIO SECUENCIA DE FIBONACCI")

x1=1
x2=1
print(x1)
print(x2)
x3=x1+x2
print(x3)
while x<1000:
    x1=x2
    x2=x3
    x3=x1+x2
    if x3>1000:
        break
    print(x3)
