"""Escribi un programa con el cual se procesaran las notas de un final de la materia. Para 
esto, se solicitara el ingreso del numero de alumno y la 
nota recibida, hasta que se ingrese un numero de alumno igual a cero, en cuyo caso se debera
imprimir en pantalla la leyenda 'La cantidad de aprobados es: ' y la cantidad de aprobados
junto con la leyenda 'La cantidad de desaprobados es: ' y la cantidad de desaprobados. 
Se debera tener en cuenta que se aprueba con una nota mayor a 4."""

numero_alumno = 1
aprobados = 0
desaprobados = 0

while numero_alumno != 0 :
    numero_alumno = int(input("ingrese su numero de alumno "))
    if numero_alumno == 0 :
       break 
    else :
        nota_recibida = int(input("Ingrese la nota recibida "))
        if nota_recibida > 4 :
            aprobados = aprobados + 1
        if nota_recibida < 4 :
            desaprobados = desaprobados + 1
    
print(f'La cantidad de aprobados es: {aprobados} ')
print(f'La cantidad de desaprobados es: {desaprobados} ')
