"""en este ejercicio se requiere ingresar el nombre de un aumno y su calificacion para luego mostrar
si esta aprobado o no, se aprueba con nota mayor a 4"""
aprobados = 0
desaprobados = 0
alumno = int(input("Ingrese numero del alumno: "))
while alumno != 0:
    nota = int(input("Ingrese la nota: "))
    if nota > 4:
        aprobados = aprobados + 1
    else: 
        desaprobados = desaprobados + 1
        alumno = int(input("Ingre numero del alumno: "))
print("La cantidad de aprobados es: ", aprobados)
print("La cantidad de desaprobados es: ", desaprobados)
    