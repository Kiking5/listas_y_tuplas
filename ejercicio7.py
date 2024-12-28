"""Escribir un programa que almacene el abecedario en una lista, elimine 
de la lista las letras que ocupen posiciones múltiplos de 3, y muestre 
por pantalla la lista resultante."""

abecedario = list("abcdefghijklmnñopqrstuvwxyz")
resultado = []
eliminadas = []

for i in range(len(abecedario)):
    if (i + 1) % 3 != 0:  # Se suma 1 al indice para que coincida con la posicion de la letra
        resultado.append(abecedario[i])  # Se agregan las letras que no son multiplos de 3
    elif (i + 1) % 3 == 0:
        eliminadas.append(abecedario[i])  # Se agregan las letras multiplos de 3

print(f"Lista resultado:\n{resultado}")
print(f"lista de eliminadas:\n{eliminadas}")
