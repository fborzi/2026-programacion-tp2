alumnos=int(input("Ingrese cantidad de alumnos:"))

aproados = 0
desaprobados = 0 

while alumnos != 0:
    nota = int(input("Ingrese la nota del alumno:"))
    if nota > 4:
        aprobados += 1
        
    else:
        desaprobados += 1

print("La cantidad de aprobados es:", aprobados)
print("La cantidad de desaprobados es:",desaprobados)