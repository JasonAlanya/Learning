lista = input("Introduzca una lista de países separados por comas: ")

lista_paises=sorted(set(lista.split(",")))

print(",".join(lista_paises))