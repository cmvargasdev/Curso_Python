class Vehiculo:
    color = 'ROJO'
    ruedas = 4
    puertas = 2

class Coche(Vehiculo):
    velocidad = 240
    cilindrada = 8

c1 = Coche()
print("El coche tiene color: "+str(c1.color))
print("El coche tiene ruedas: "+str(c1.ruedas))
print("El coche tiene puertas: "+str(c1.puertas))
print("El coche tiene velocidad: "+str(c1.velocidad))
print("El coche tiene cilindrada: "+str(c1.cilindrada))
