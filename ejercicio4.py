"""Escribir un programa que pregunte al usuario los números ganadores de la 
lotería primitiva, los almacene en una lista y los muestre por pantalla 
ordenados de menor a mayor."""

ganadores = []
for numero in range(6):
    ganadores.append(int(input("Introduce un numero ganador: ")))
ganadores.sort()
print(f"Los números ganadores fueron: {ganadores}")