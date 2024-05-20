# Solicitar al usuario ingresar el RUT de largo 8
rut = input("Ingrese el RUT (sin dígito verificador) de largo 8: ")

# Verificar que el RUT tenga la longitud correcta
if len(rut) != 8:
    print("El RUT debe tener 8 dígitos.")
else:
    # Calcular el dígito verificador
    multiplicador = [2, 3, 4, 5, 6, 7, 2, 3]
    suma = 0
    for i in range(8):
        suma += int(rut[7 - i]) * multiplicador[i]

    resto = suma % 11
    digito_verificador = 11 - resto

    # Si el resultado es 10, el dígito verificador es 'K'
    if digito_verificador == 10:
        print("El dígito verificador es: K")
    # Si el resultado es 11, el dígito verificador es '0'
    elif digito_verificador == 11:
        print("El dígito verificador es: 0")
    # Para cualquier otro caso, el dígito verificador es el número obtenido
    else:
        print("El dígito verificador es:", digito_verificador)