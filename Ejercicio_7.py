class Alumno():
    def __init__(self, nombre, nota):
        self.nombre   = nombre
        self.nota = nota

    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)

    def isAprobado(self):
            if self.nota < 10:
                print("Alumno No Aprobado")
            else:
                print("Alumno Aprobado")


alumno = Alumno("Miguel", 9)
alumno.imprimir()
alumno.isAprobado()
