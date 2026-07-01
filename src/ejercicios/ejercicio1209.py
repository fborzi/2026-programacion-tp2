aprobados = 0
desaprobados = 0
while True:
    numero_alumno = int(input("Ingrese el numero de alumno (0 para terminar): "))
    
    if numero_alumno == 0:
        break  
    
    nota = int(input("Ingrese la nota del alumno: "))
    
    if nota > 4:
        aprobados += 1
    else:
        desaprobados += 1

print("La cantidad de aprobados es:", aprobados)
print("La cantidad de desaprobados es:", desaprobados)
