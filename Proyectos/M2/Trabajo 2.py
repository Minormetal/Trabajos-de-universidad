# Se utiliza un bucle while para solicitar al usuario que ingrese un número entero del 1 al 9.
# Se utiliza un bucle infinito con una condición para verificar si el número ingresado está dentro del rango requerido.
# Si el usuario ingresa un valor no numérico o fuera del rango, se muestra un mensaje de error y se solicita nuevamente el ingreso.
while True:
    try:
        numero_inicial = int(input("Ingrese un número entero del 1 al 9: "))
        if 1 <= numero_inicial <= 9:
            break
        else:
            print("Error: Debe ingresar un número entre 1 y 9.")
    except ValueError:
        print("Error: Debe ingresar un número entero.")

# Una vez que se ha ingresado un número válido, se utiliza un bucle for para iterar sobre los números del 1 al 9.
# Dentro de este bucle, se verifica si cada número es múltiplo del número inicial utilizando el operador %.
# Si no es un múltiplo, se solicita al usuario que ingrese ese número.
# Se utiliza otro bucle while para asegurarse de que el usuario ingrese el número correcto.
# Si el usuario ingresa un valor incorrecto, se muestra un mensaje de error y se solicita nuevamente el ingreso.
for i in range(1, 10):
    if i % numero_inicial != 0:
        while True:
            try:
                numero_ingresado = int(input(f"Ingrese el número {i}: "))
                if numero_ingresado == i:
                    break
                else:
                    print(f"Error: Debe ingresar el número {i}.")
            except ValueError:
                print("Error: Debe ingresar un número entero.")

# Una vez que el usuario ha ingresado todos los números correctamente, el programa muestra un mensaje de que ha finalizado correctamente.
print("Programa finalizado correctamente.")