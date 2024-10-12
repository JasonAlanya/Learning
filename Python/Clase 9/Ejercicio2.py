from functools import reduce


lista_numeros=[2,5,3,8,9]

lista_impares=list(filter(lambda n:n%2,lista_numeros))

suma=reduce(lambda n1,n2:n1+n2,lista_impares)

print(f"La suma de los números impares de la lista es: {suma}")