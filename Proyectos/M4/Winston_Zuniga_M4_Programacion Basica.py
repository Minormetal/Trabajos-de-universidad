"""ITEM 1 - Programa Evaluador de Seguridad de Contraseñas."""

# Mensaje de bienvenida.
print("Bienvenido al Programa Evaluador de Seguridad de Contraseñas.")

"""
Este programa evalúa la seguridad de una contraseña a través de cuatro funciones, asegurando
que contenga al menos una letra mayúscula (evaluada por la función contiene_letra_mayuscula),
al menos una letra minúscula (evaluada por la función contiene_letra_minuscula), y al menos un número
(evaluada por la función contiene_numero).
La función seguridad_contraseña evalúa el cumplimiento de las otras 3 condiciones e imprime mensajes de error.
La función principal solicita la contraseña al usuario y luego llama a la función.
"""

def contiene_letra_mayuscula(contraseña): # Evalúa la presencia de una letra mayúscula.

    for caracter in contraseña:
        if caracter.isupper():
            return True
    return False

def contiene_letra_minuscula(contraseña): # Evalúa la presencia de una letra minúscula.

    for caracter in contraseña:
        if caracter.islower():
            return True           
    return False

def contiene_numero(contraseña): # Evalúa la presencia de un número.
    
    for caracter in contraseña:
        if caracter.isdigit():
            return True  
    return False
    

def seguridad_contraseña(contraseña): # Evalúa la seguridad global con cumplimiento de 3 condiciones base.
    tiene_mayuscula = contiene_letra_mayuscula(contraseña)
    tiene_minuscula = contiene_letra_minuscula(contraseña)
    tiene_numero = contiene_numero(contraseña)

    if tiene_mayuscula and  tiene_minuscula  and  tiene_numero:
        return True
    else:
        print("La contraseña no cumple con las siguientes condiciones:")
        if not tiene_mayuscula:
            print("La contraseña debe contener al menos una letra mayúscula")
        if not tiene_minuscula:
            print("La contraseña debe contener al menos una letra minúscula")
        if not tiene_numero:
            print("La contraseña debe contener al menos un número")
        return False
    
def principal():
    while True:
        # Solicitar la contraseña al usuario.
        contraseña = input("Ingrese su contraseña: ")

        if seguridad_contraseña(contraseña):
            print("La contraseña es segura.")
        else:
            print("La contraseña no es segura.")

        siguiente_contraseña = input("¿Desea evaluar otra contraseña? (s/n): ")
        
        if siguiente_contraseña.lower() != 's':
            print("Gracias por utilizar el Programa Evaluador de Seguridad de Contraseñas.")
            break

# Llamar a la función principal.
if __name__ == "__main__":
    principal()


"""ELEMENTO 2 - Calculadora de Totales.

Este programa te permite ingresar una lista de números para sumarlos y obtener el total.
La función calcular_total utiliza recursión para sumar los números de la lista uno por uno.
Pide al usuario que ingrese un número o presione espacio para finalizar.
Si se presiona espacio como primer dato, devuelve cero.

"""

# Mensaje de bienvenida.
print("¡Bienvenido a la Calculadora de Totales!")

def calcular_total(total=0):
    # Solicita al usuario ingresar un número o espacio.
    ingreso = input("Ingrese un número (o espacio para terminar): ")
    
    # Si se presiona espacio, devuelve el total.
    if ingreso == " ":
        return total
    # Si se presiona espacio como primer dato, devuelve 0.
    elif ingreso.strip() == '' and total == 0:
        return 0 
    else:
        try:
            num = float(ingreso) 
            return num + calcular_total()  # Utiliza recursión para sumar el número al total.
        except ValueError:
            # Si lo ingresado no es válido, muestra un mensaje de error.
            print("Entrada no válida. Ingrese un número (o espacio para terminar).")
            # Llama de nuevo a la función sin afectar el total.
            return calcular_total(total) 
        
# Llama a la función para calcular el total y lo muestra.
resultado = calcular_total()
print("El total de la suma es: ", resultado)

print("¡Gracias por usar la Calculadora de Totales!")



"""ITEM 3 - Programa Bancario Simplificado."""

# Mensaje de bienvenida.
print("¡Bienvenido al Programa Bancario Básico!")

# Definir la clase Cuenta
class Cuenta:
    def __init__(self, numero_cuenta, nombre_titular, tipo_cuenta):
        # Validar datos de entrada
        if not numero_cuenta.isdigit() or not nombre_titular.isalpha() or not tipo_cuenta.isalpha():
            raise ValueError("Los datos ingresados no son válidos.")

        # Inicializar atributos
        self.numero_cuenta, self.nombre_titular, self.tipo_cuenta, self.saldo = numero_cuenta, nombre_titular, tipo_cuenta, 0

    def depositar(self, monto):
        # Método para realizar un depósito
        if monto > 0:
            self.saldo += monto
            print(f"Depósito de {monto}. Nuevo saldo de {self.nombre_titular}: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, monto):
        # Método para realizar un retiro
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de {monto}. Nuevo saldo de {self.nombre_titular}: {self.saldo}")
        else:
            print("No se puede retirar esa cantidad o saldo insuficiente.")

    def obtener_balance(self):
        # Método para obtener el balance actual
        print(f"Titular: {self.nombre_titular}\nNúmero de Cuenta: {self.numero_cuenta}\nTipo de Cuenta: {self.tipo_cuenta}\nSaldo: {self.saldo}")

def gestionar_cuenta(cuenta):
    # Menú de opciones
    opciones = {'1': cuenta.obtener_balance, '2': lambda: cuenta.depositar(float(input("Ingrese monto a depositar: "))),
                '3': lambda: cuenta.retirar(float(input("Ingrese monto a retirar: "))), '4': exit}
    
    while True:
        # Mostrar menú y procesar opción seleccionada
        print("\nMenú:\n1. Mostrar saldo\n2. Realizar depósito\n3. Realizar retiro\n4. Salir")
        opcion = input("Seleccione una opción (1/2/3/4): ")
        opciones.get(opcion, lambda: print("Opción no válida."))()
        # Consultar si el usuario desea continuar
        continuar = input("¿Desea realizar otra operación? (S/N): ").strip().upper()
        if continuar != 'S':
            break

try:
    # Ingresar datos de la cuenta y gestionarla
    print("Por favor ingrese los datos de la cuenta.")
    numero_cuenta = input("Número de cuenta: ")
    nombre_titular = input("Nombre del titular: ")
    tipo_cuenta = input("Tipo de cuenta (Ahorro/Corriente/Inversiones): ")

    cuenta = Cuenta(numero_cuenta, nombre_titular, tipo_cuenta)
    gestionar_cuenta(cuenta)
except ValueError as e:
    # Capturar errores de validación
    print(f"Error: {e}")
except KeyboardInterrupt:
    # Capturar interrupción de teclado
    print("\n¡Gracias por usar el Programa Bancario Básico!")