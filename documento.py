import math as mt 

r=input("asigne el valor de la distancia  r:")
r=float(r)
angulo=input("asigne el valor del angulo:")
angulo=float(angulo)
a=(mt.pi*angulo)/180
z=input("asigne el valor de z:")
z=float(z)

print("el valor en la coordenada x es:")
x=r*(mt.cos(a))
print(x)
print("el valor en la coordenada y es:")
y=r*(mt.sin(a))
print(y)
print("el valor en la coordenada z es:")
print(z)






