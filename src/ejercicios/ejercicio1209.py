"""Este programa  solicita el ingreso del numero de alumno y su nota recibida
hasta que se ingrese un numero de alumno igual a 0,la leyenda debera imprimir la cantidad de alumnos aprobados,
y la cantidad de alumnos desaprobados, se debera tener en cuenta que se aprueba con una nota mayor a 4."""


alumno = int(input("Ingrese el numero del alumno: "))
nota = float(input("Ingrese la nota del alumno: "))

aprobados = 0
desaprobados = 0

while alumno != 0:
    if nota > 4:
        aprobados = aprobados + 1
    else: 
        desaprobados = desaprobados + 1
       
    alumno = int(input("Ingrese el numero del alumno: "))
    nota = float(input("Ingrese la nota del alumno: ")) 


print("La cantidad de aprobados es : ",aprobados)
print("La cantidad de desaprobados es: ",desaprobados)

  

