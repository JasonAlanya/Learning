def validar_numero_primo():
    numero=int(input("Ingrese un número: "))
    i=2
    primo=True

    while i<numero:
        if numero%i==0:
            primo=False
            break
        i+=1

    if primo==True:
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} no es primo")

validar_numero_primo()