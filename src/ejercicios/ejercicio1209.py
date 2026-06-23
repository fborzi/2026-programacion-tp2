"""inicialice numero_alumno en 1 para entrar al bucle y los contadores aprobados y desaprobados en cero.
utilice un while que se repite mientras numero_alumno sea distinto de cero, pero como el ingreso del 
numero de alumno ocurre dentro del bucle necesito verificar inmediatamente si es cero para no seguir
pidiendo la nota, por eso utilice un break que corta el while en ese momento. si el numero es valido
solicito la nota y la clasifico como aprobado si es mayor a 4 o desaprobado si es menor a 4.
al finalizar imprimo la cantidad de aprobados y desaprobados."""

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
