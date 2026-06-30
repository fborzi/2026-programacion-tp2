aprobados=0
desaprobado=0
alumno=int(input("ingrese el numero de alumno:"))
while alumno!=0:
    nota=int(input("ingrese la nota del alumno:"))
    if nota>=4:
        aprobados+=1
        alumno=int(input("ingrese el numero de alumno:"))
    else: 
        desaprobado+=1
        alumno=int(input("ingrese el numero de alumno:"))
  

print("la cantidad de alumnos aprobados es:", aprobados)
print("la cantidad de alumnos desaprobados es:", desaprobado)