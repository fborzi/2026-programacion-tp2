# Inicializar contadores
aprobados = 0
desaprobados = 0

# Leer número de alumno
numero_alumno = int(input("Ingrese número de alumno (0 para finalizar): "))

while numero_alumno != 0:
    nota = float(input("Ingrese la nota del alumno: "))

    if nota > 4:
        aprobados += 1
    else:
        desaprobados += 1

    numero_alumno = int(input("Ingrese número de alumno (0 para finalizar): "))

# Mostrar resultados
print("La cantidad de aprobados es:", aprobados)
print("La cantidad de desaprobados es:", desaprobados)