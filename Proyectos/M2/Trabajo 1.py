# Saludo inicial.
print("¡Bienvenido al Programa de Matrices!")

# Solicitamos al usuario el número de filas y columnas para dibujar la matriz.
filas = int(input("Por favor, ingrese el número de filas de la matriz: "))
columnas = int(input("Ahora, ingrese el número de columnas de la matriz: "))

# DEFINIMOS UNA FUNCIÓN PARA IMPRIMIR UNA MATRIZ DE FILAS Y COLUMNAS DETERMINADAS.
"""
La función 'crear_matriz' imprime una matriz con el número de filas y columnas especificado.
Primero se imprime la parte superior de la matriz, luego se imprime el contenido de cada fila,
y finalmente se imprime la parte inferior de la matriz.
"""
def crear_matriz(filas, columnas):
    for i in range(filas):   
        # Imprime la parte superior de la fila
        print("+---" * columnas + "+")
        # Imprime el contenido de la fila
        print("|   " * columnas + "|")
    # Imprime la parte inferior de la matriz.
    print("+---" * columnas + "+")

# Llamamos a nuestra función para crear y mostrar la matriz.
crear_matriz(filas, columnas)