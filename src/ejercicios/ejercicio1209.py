corte = int(input("Ingrese el numero de alumno:"))
aprobados = 0
desaprobados=0

while corte != 0 :
    nota = int(input("Ingrese la nota:"))
    if nota > 4 :
        aprobados = aprobados + 1
        
    else :
        desaprobados= desaprobados + 1
    corte = int(input("Ingrese el numero de alumno:")) 
print("La cantidad de aprobados es:", aprobados)
print("La cantidad de desaprobados es:", desaprobados)