"""inicialice numero en 1 para que entre en el bucle, y primo en cero para utilizarlo mas adelante como contador
en la suma que va a almacenar el conteo de numeros primos que aparezcan
utilice un while para que repita la accion hasta que el usuario ingrese un CERO.
Utilice la condicional para validar que el numero sea mayor a 1, inicialice es_primo en true para que al cumplirse
que el numero sea divisible entre dos cambie automaticamente a false y en la siguiente condicional, utilice el for
para que verifique en cada ingreso si el numero ingresado es divisible o no, si lo es entonces es_primo pasa a 
ser false y continua la vuelta desde el inicio. Por ultimo sumo 1 numero al contador si es_primo es true"""

numero = 1
primo = 0 

while numero != 0:
    numero = int(input("ingrese un numero mayor que 1: "))
    if numero > 1:
        es_primo = True
        for i in range(2, numero):
            if numero % i == 0:
                es_primo = False
        if es_primo:
            primo = primo + 1

print(f"Cantidad de numeros primos ingresados: {primo}")
       