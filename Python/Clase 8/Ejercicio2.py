from copyreg import pickle
from pickle import *

class Vehiculo:
    Color=""
    Ruedas=0
    Puertas=0

vehiculo=Vehiculo()
vehiculo.Color="Rojo"
vehiculo.Ruedas=4
vehiculo.Puertas=5

archivo = open('Clase 8/nuevo_archivo2.txt', 'wb')
dump(vehiculo,archivo)
archivo.close()


archivo=open('Clase 8./nuevo_archivo2.txt', 'rb')
coche=load(archivo)
print(f"El vehículo es de color: {coche.Color}\nTiene {coche.Ruedas} ruedas\nTiene {coche.Puertas} puertas")
archivo.close()