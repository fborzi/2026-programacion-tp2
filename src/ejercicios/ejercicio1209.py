numero_alumno = int(input("Ingrese numero de alumno:"))

aprobados = 0
desaprobados = 0

while numero_alumno != 0:
    nota = int(input("Ingrese la nota:"))

    if nota > 4:
        aprobados += 1
    else:
        desaprobados += 1

    numero_alumno = int(input("Ingrese numero de alumno: "))

print("La cantidad de aprobados es:", aprobados)
print("La cantidad de desaprobados es:", desaprobados)