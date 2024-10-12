class Alumno:
    nombre=None
    nota=None
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def verificar_nota(self):
        if(self.nota<5):
            print(f"El alumno {self.nombre} está desaprobado")
        else:
            print(f"El alumno {self.nombre} está aprobado")

juan=Alumno("Juan",3)

juan.verificar_nota()