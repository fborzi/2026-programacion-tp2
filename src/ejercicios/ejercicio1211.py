contador = 0

ceros = 0
positivos = 0
contadorPromedio = 0
contadorNegativos= 0
promedio = 0

while contador < 20 :
    numero = int(input("Ingrese un numero entero entre (-10 y 10):"))
    if -10 < numero < 10 :
        if numero == 0 :
            ceros = ceros + 1
            contador= contador + 1
        elif numero > 0 :
            positivos = numero + positivos
            contadorPromedio= contadorPromedio +1
            promedio= positivos/contadorPromedio
            contador = contador + 1
        else : 
            contadorNegativos = contadorNegativos + numero
            contador = contador + 1
        
    else : 
        print("numero fuera de rango")
print("La cantidad de ceros ingresados es:", ceros)
print("La suma de los numeros negativos es:", contadorNegativos)     
print("El promedio de los positivos es:", promedio)