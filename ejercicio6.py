"""Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una 
lista, pregunte al usuario la nota que ha sacado en cada asignatura 
y elimine de la lista las asignaturas aprobadas. Al final el programa 
debe mostrar por pantalla las asignaturas que el usuario tiene que repetir."""

asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

notas = [float(input("¿Qué nota has sacado en Matemáticas?: ")),
         float(input("¿Qué nota has sacado en Física?: ")),
         float(input("¿Qué nota has sacado en Química?: ")),
         float(input("¿Qué nota has sacado en Historia?: ")),
         float(input("¿Qué nota has sacado en Lengua?: "))]

# Crear una lista temporal para las asignaturas aprobadas
asignaturas_aprobadas = [asignaturas[i] for i in range(len(asignaturas)) if notas[i] >= 5]

# Eliminar las asignaturas aprobadas de la lista original
for aprobada in asignaturas_aprobadas:
    asignaturas.remove(aprobada)

print(f"Tienes que repetir las siguientes asignaturas: {asignaturas}")
