import math
##Implementación de las funciones

def area_triangulo (base,altura):
    area=base*altura/2
    return area

def area_circulo(radio):
    area=math.pi*(radio**2)
    return area

print("El area del triángulo es: ",area_triangulo(12.5,4))
print("El area del círculo es: ",area_circulo(10.6))