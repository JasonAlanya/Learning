archivo = open('Clase 8/nuevo_archivo.txt', 'w')
archivo.write('Hola mundo\n')
archivo.close()

archivo= open('Clase 8./nuevo_archivo.txt', 'a')
archivo.write('Adios mundo')
archivo.close()

archivo=open('Clase 8./nuevo_archivo.txt', 'r')
print(archivo.read())
archivo.close()