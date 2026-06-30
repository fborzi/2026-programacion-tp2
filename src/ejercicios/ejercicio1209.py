aprobados = 0
desaprobados = 0

while True:
    numero_alumno = int(input())
    
    if numero_alumno == 0:
        break
    
    nota = int(input())
    
    if nota > 4:
        aprobados = aprobados + 1
    else:
        desaprobados = desaprobados + 1
        
print("la cantidad de aprobados es: {aprobados}")
print("la cantidad de desaprobados es: {desaprobados}")        