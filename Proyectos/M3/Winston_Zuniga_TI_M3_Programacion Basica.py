"""ITEM 1 - Programa para ordenar números de mayor a menor."""

# Mensaje de bienvenida.
print("Bienvenido al Programa de Ordenamiento de Números de Mayor a Menor")

""" 
Este programa genera una lista vacía para almacenar los números ingresados por el usuario y
luego los muestra ordenados de mayor a menor, pidiendo un ingreso mínimo de 10 números y 
un máximo de 20.
Establecemos la función para ingreso y una función para ordenar y mostrar.
"""


# Inicializamos una lista vacía para almacenar los números ingresados.
def ingresar_numeros():
    numeros = []

# Pedimos al usuario que ingrese números hasta que ingrese 0 o alcancemos el límite.

    while len(numeros) < 20:
        ingreso = input("Ingrese un número (0 para finalizar): ")

        if ingreso.isdigit(): # Verificamos si la entrada es un número
            numero = int(ingreso)

            if numero == 0: 
                break # Salir del bucle si el usuario ingresa 0
            else:
                numeros.append(numero) # Agregar el número a la lista
        else:
            print("Por favor, ingrese un número válido.")

    if len(numeros) > 20:
        print("Máximo 20 números.")
            

    if len(numeros) < 10:
        print("No se ingresaron suficientes números (mínimo 10).")
    
    return numeros

# Verificamos si se ingresaron suficientes números.
def orden_mostrar(numeros):
    if len(numeros) >= 10:  # Establecemos un límite mínimo de 10.
        numeros.sort(reverse=True) # Ordenamos la lista de números de mayor a menor.
        print("Números ordenados de mayor a menor:") # Mostramos la lista ordenada sin incluir el 0
        for num in numeros:
            print(num)

def principal():
    numeros = ingresar_numeros()

    if numeros:
        orden_mostrar(numeros)

if __name__ == "__main__":
    principal()



"""SECCIÓN A - Programa de registro de palabras."""

# Mensaje de inicio.
print("¡Hola! Bienvenido al Programa de Registro de Palabras.")

"""
Este script importa un módulo de expresiones regulares para validar las palabras ingresadas.
Finaliza el bucle de entrada de palabras cuando se introduce el símbolo '###', luego muestra las palabras ingresadas sin repeticiones.
"""

import re  # Importa el módulo 're' (expresiones regulares) para validar palabras.

def validar_palabra(cadena):
    # Utiliza una expresión regular para verificar si la cadena contiene solo letras.
    return bool(re.match("^[a-zA-Z]+$", cadena))

def ingresar_palabras():
    palabras = set()
    
    while True:
        palabra = input("Por favor, ingresa una palabra o '###' para terminar: ")
        
        if palabra == '###':
            break
         
        if validar_palabra(palabra):
            palabras.add(palabra)
        else:
            print("¡Ups! Parece que ingresaste una palabra no válida.")

    return palabras

def mostrar_palabras_unicas(palabras):
    print("¡Aquí están las palabras que ingresaste sin duplicados!") 
    for palabra in palabras:
        print(palabra)

def ejecutar_programa():
    palabras = ingresar_palabras()
    mostrar_palabras_unicas(palabras)

if __name__ == "__main__":
    ejecutar_programa()
    
    
    
    
    """SCRABBLE - El Juego de las Palabras Cruzadas"""

# Mensaje de bienvenida.
print("¡Bienvenido al Juego de Scrabble!")

"""
Este script comienza creando un diccionario (puntajes) con valores asignados a las letras
para calcular el puntaje obtenido por cada palabra ingresada. Además, se valida el ingreso
de palabras y muestra un mensaje de error en caso de una entrada no válida.
También se agrega una consulta booleana para validar el ingreso de una nueva palabra.

"""

# Creamos un diccionario con los valores de las letras
puntajes = {
    'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
    'D': 2, 'G': 2,
    'B': 3, 'C': 3, 'M': 3, 'P': 3,
    'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
    'K': 5,
    'J': 8, 'X': 8,
    'Q': 10, 'Z': 10
}

def calculador_puntaje(palabra):
    puntaje_total = 0
    for letra in palabra:
        # Verifica si la letra está en el diccionario y es una letra válida
        if letra.upper() in puntajes:
            puntaje_total += puntajes[letra.upper()]
        else:
            print(f"La letra '{letra}' no es válida.")
            return 0  # Si se ingresa una letra no válida, el puntaje es cero
    return puntaje_total

while True:
    palabra = input("Ingresa una palabra o frase (solo letras y espacios): ")
    
    if palabra.isalpha() or palabra.isspace():
        # Calcular el puntaje de la palabra o frase
        puntaje = calculador_puntaje(palabra)
        print(f"Puntaje total: {puntaje}")
    else:
        print("Ingresa solo letras y espacios.")
    
    otra_palabra = input("¿Deseas ingresar otra palabra o frase? (S/N): ")
    if otra_palabra.upper() != "S":
        print("Gracias por jugar al Scrabble.")
        break
    


"""ITEM 4 - Identificador de Anagramas."""

# Mensaje de bienvenida.
print("¡Bienvenido al Identificador de Anagramas!")

"""
Este programa permite determinar si dos palabras ingresadas por el usuario son anagramas.

La función is_palabra valida que solo se ingresen letras (sin números ni caracteres especiales).
La función son_anagramas(palabra1, palabra2) verifica si las palabras ingresadas son anagramas.
"""

def is_palabra(palabra):
    # Valida si la palabra contiene solo letras
    return palabra.isalpha()

def son_anagramas(palabra1, palabra2):
    # Corrobora si ambas palabras tienen la misma longitud
    if len(palabra1) != len(palabra2):
        return False

    # Creamos diccionarios para contar la frecuencia de letras en ambas palabras
    freq_palabra1 = {}
    freq_palabra2 = {}

    # Contamos la frecuencia de letras en palabra1
    for letra in palabra1:
        if letra in freq_palabra1:
            freq_palabra1[letra] += 1
        else:
            freq_palabra1[letra] = 1

    # Contamos la frecuencia de letras en palabra2
    for letra in palabra2:
        if letra in freq_palabra2:
            freq_palabra2[letra] += 1
        else:
            freq_palabra2[letra] = 1

    # Validamos si los diccionarios son iguales (mismas letras con la misma frecuencia)
    return freq_palabra1 == freq_palabra2

# Solicitamos ingreso de palabras al usuario.
def principal():
    palabra1 = input("Ingrese la primera palabra: ").strip()
    palabra2 = input("Ingrese la segunda palabra: ").strip()

    # Valida que lo ingresado sean palabras
    if not (is_palabra(palabra1) and is_palabra(palabra2)):
        print("Por favor, ingrese solo palabras válidas.")
        return

    if son_anagramas(palabra1, palabra2):
        print(f"{palabra1} y {palabra2} son anagramas.")
    else:
        print(f"{palabra1} y {palabra2} no son anagramas.")

if __name__ == "__main__":
    principal()



"""ITEM 5 - Programa de Sumatoria."""

# Mensaje de bienvenida.
print("¡Bienvenido al Programa de Sumatoria!")

"""
Este programa devuelve la suma de los números ingresados por el usuario.

La función obtener_numero solicita al usuario que ingrese un número y lo devuelve como un entero.
Si la entrada no es un número válido, muestra un mensaje de error y devuelve 0.

La función sumar_numeros solicita al usuario números hasta que presiona Enter sin ingresar nada.
Luego muestra la suma total de los números ingresados.

"""

def obtener_numero():
    ingreso = input("Ingrese un número (o presione Enter para finalizar): ")
    try:
        numero = int(ingreso)
        return numero
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        return 0

def sumar_numeros():
    suma_total = 0
    while True:
        numero = obtener_numero()
        if numero == 0:
            continue
        suma_total += numero
        print("Suma parcial:", suma_total)
        if input("¿Deseas ingresar otro número? (s=si, espacio=no): ").strip().lower() != "s":
            break

    print("La suma total de los números ingresados es:", suma_total)
    print("¡Gracias por usar el programa de sumatoria!")

# Llamamos a la función principal para ejecutar el programa.
sumar_numeros()