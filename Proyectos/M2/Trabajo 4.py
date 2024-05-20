# Se utiliza un bucle while para permitir al usuario elegir dos palabras que cumplan con las condiciones mencionadas.
# Se verifica que las palabras tengan el mismo largo y que no tengan letras iguales en la misma posición.
while True:
    palabra1 = input("Ingrese la primera palabra: ")
    palabra2 = input("Ingrese la segunda palabra: ")
    
    if len(palabra1) == len(palabra2) and not any(palabra1[i] == palabra2[i] for i in range(len(palabra1))):
        break
    else:
        print("Error: Las palabras deben tener el mismo largo y no pueden tener letras iguales en la misma posición.")

# Se solicita al usuario que ingrese una frase.
frase = input("Ingrese una frase: ")

# Se utiliza un bucle for para iterar sobre cada letra de la frase.
# Se comprueba si la letra está en alguna de las dos palabras elegidas.
# Si está en la primera palabra, se reemplaza por la letra correspondiente en la segunda palabra, y viceversa.
# Si la letra no está en ninguna de las dos palabras, se deja sin cambios.
nueva_frase = ""
for letra in frase:
    if letra in palabra1:
        nueva_letra = palabra2[palabra1.index(letra)]
    elif letra in palabra2:
        nueva_letra = palabra1[palabra2.index(letra)]
    else:
        nueva_letra = letra
    nueva_frase += nueva_letra

# Se imprime la nueva frase con las letras reemplazadas.
print("La nueva frase con las letras reemplazadas es:")
print(nueva_frase)