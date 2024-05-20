import datetime  # Importamos el módulo datetime para trabajar con fechas

# Paso 1: Solicitar al usuario el año de nacimiento de la persona.
while True:
    try:
        año_nacimiento = int(input("Ingrese el año de nacimiento de la persona: "))
        if año_nacimiento > 0:
            break
        else:
            print("Error: El año de nacimiento debe ser un número positivo.")
    except ValueError:
        print("Error: Debe ingresar un año válido.")

# Paso 2: Solicitar al usuario el año de muerte de la persona.
while True:
    try:
        año_muerte = int(input("Ingrese el año de muerte de la persona (Ingrese 0 si está viva): "))
        if año_muerte >= 0:
            break
        else:
            print("Error: El año de muerte debe ser un número positivo o 0.")
    except ValueError:
        print("Error: Debe ingresar un año válido.")

# Si la persona está viva, se reemplaza el año de muerte por el año actual.
if año_muerte == 0:
    año_muerte = datetime.datetime.now().year

# Paso 4: Calcular la cantidad de años bisiestos que la persona ha vivido.
años_bisiestos = 0
for año in range(año_nacimiento, año_muerte + 1):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        años_bisiestos += 1

# Paso 5: Mostrar la cantidad de años bisiestos calculados en el paso anterior.
print(f"La persona ha vivido durante {años_bisiestos} años bisiestos.")