numero1=input("Ingrese el rango inferior: ")
numero2=input("Ingrese el rango superior: ")

numeros_impares=[]

for numero in range(int(numero1),int(numero2)+1):
    if numero%2!=0:
        numeros_impares.append(numero)


print(numeros_impares)
