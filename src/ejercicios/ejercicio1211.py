"""inicialice los contadores en cero para acumular los valores durante el recorrido.
utilice un for para solicitar 20 numeros, si el numero esta dentro del rango entre -10 y 10 inclusive
lo clasifico en negativo, cero o positivo y actualizo el contador o suma correspondiente,
si esta fuera del rango aviso al usuario pero no repito el ingreso. al finalizar imprimo
la sumatoria de negativos, la cantidad de ceros y el promedio de los positivos."""

numeros_enteros = 0
cantidad_cero = 0
suma_positivos = 0
suma_negativos = 0
total = 0

for i in range(20):
    numeros_enteros = int(input("ingrese numero entero"))
    if numeros_enteros >= -10 and numeros_enteros <= 10:
        if numeros_enteros < 0:
            suma_negativos = suma_negativos + numeros_enteros
        elif numeros_enteros == 0:
            cantidad_cero = cantidad_cero + 1
        else:
            numeros_enteros > 0
            suma_positivos = suma_positivos + numeros_enteros
            total = total + 1
            promedio = suma_positivos / total
    else:
        print("Numero fuera de rango intente nuevamente")

print(f"La cantidad de numeros negativos es: {suma_negativos}")
print(f"La cantidad de ceros es: {cantidad_cero}")
print(f"El promedio de los numeros positivos ingresados es: {promedio}")
