"""Este programa procesa las notas obtenidas por los alumnos en un
examen final, solicitando el número de alumno y su calificación hasta
que se ingrese un número de alumno igual a cero. Durante el proceso
se contabiliza la cantidad de alumnos aprobados y desaprobados,
considerando aprobados a quienes obtuvieron una nota mayor a 4,
para luego mostrar los resultados finales."""

aprobados = 0
desaprobados = 0

alumno = int(input("Ingrese el número de alumno seguido de su nota: "))

while alumno != 0:
    nota = int(input())

    if nota > 4:
        aprobados += 1
    else:
        desaprobados += 1

    alumno = int(input())

print("La cantidad de aprobados es:", aprobados)
print("La cantidad de desaprobados es:", desaprobados)