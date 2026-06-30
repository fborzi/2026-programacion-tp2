# Escribi un programa que solicita el número de un alumno y su nota,
# luego pidd el número y la nota de otro alumno y así sucesivamente hasta que
# se ingrese el número 0. Finalmente, el programa debe mostrar la cantidad de alumnos aprobados y desaprobados."

numero = 0
nota = 0
contadorapro = 0
contadordes = 0

numero = int(input("Ingrese el numero del alumno o 0 para terminar: "))

while numero != 0:
    nota = int(input("Ingrese la nota del alumno: "))
    if nota > 4:
        contadorapro = contadorapro + 1
    elif nota <= 4 and nota > 0:
        contadordes = contadordes + 1
    numero = int(input("Ingrese el numero del alumno o 0 para terminar: "))

print("La cantidad de alumnos aprobados es:", contadorapro)
print("La cantidad de alumnos desaprobados es:", contadordes)
