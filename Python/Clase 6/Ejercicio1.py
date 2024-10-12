class Vehiculo:
    Color=""
    Ruedas=0
    Puertas=0

class Coche(Vehiculo):
    Velocidad=0
    Cilindrada=0

    def imprimir_caracteristicas(self):
        print(f"Color del coche: {self.Color}")
        print(f"Cantidad de ruedas del coche: {self.Ruedas}")
        print(f"Cantidad de puertas del coche: {self.Puertas}")
        print(f"Velocidad del coche: {self.Velocidad} km/h")
        print(f"Cilindrada del coche: {self.Cilindrada} cc")

nuevocoche=Coche()
nuevocoche.Color="Rojo"
nuevocoche.Ruedas=4
nuevocoche.Puertas=5
nuevocoche.Velocidad=120
nuevocoche.Cilindrada=1600
nuevocoche.imprimir_caracteristicas()