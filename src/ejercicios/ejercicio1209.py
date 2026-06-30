"""En este ejercicio pediremos ingresar un numero de alumno en conjunto con la nota de la evaluacion 
luego evalaremos si aprobo el examen e imprimiremos cantidad de alumnos aprobados y cantidad desaprobados"""
aprobados = 0
desaprobados = 0

legajo = int(input("ingrese numero de legajo del alumno: "))

while legajo != 0:
    nota = int(input("ingrese nota de la evaluacion: "))

    if nota > 4:
        aprobados += 1
    else:
        desaprobados += 1

    legajo = int(input("ingrese numero de legajo del alumno"))

print("La cantidad de aprobados es:", aprobados)
print("La cantidad de desaprobados es:", desaprobados)