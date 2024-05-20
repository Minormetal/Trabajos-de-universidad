# Solicitar al usuario ingresar las notas de las evaluaciones
lab1 = float(input("Ingrese la nota del Laboratorio 1: "))
lab2 = float(input("Ingrese la nota del Laboratorio 2: "))
lab3 = float(input("Ingrese la nota del Laboratorio 3: "))
tarea1 = float(input("Ingrese la nota de la Tarea 1: "))
tarea2 = float(input("Ingrese la nota de la Tarea 2: "))
tarea3 = float(input("Ingrese la nota de la Tarea 3: "))
solemne1 = float(input("Ingrese la nota del Solmene 1: "))
solemne2 = float(input("Ingrese la nota del Solmene 2: "))

# Calcular el promedio de laboratorios y tareas
prom_lab = (lab1 + lab2 + lab3) / 3
prom_tareas = (tarea1 + tarea2 + tarea3) / 3

# Calcular la nota de presentación
nota_presentacion = prom_lab * 0.15 + prom_tareas * 0.15 + solemne1 * 0.35 + solemne2 * 0.35

# Mostrar el resultado en pantalla
print("Nota de presentación =", nota_presentacion)