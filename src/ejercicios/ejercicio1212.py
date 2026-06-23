"""inicialice es_primo en true para asumir que el numero es primo, utilice un for para recorrer
todos los valores desde 2 hasta el numero menos 1, si alguno divide exacto al numero entonces
es_primo pasa a false. por ultimo evaluo es_primo para imprimir si el numero es primo o no."""

numero = int(input("ingrese un numero mayor que 1: "))
es_primo = True

for i in range(2, numero):
    if numero % i == 0:
        es_primo = False

if es_primo:
    print(f"El numero {numero} es PRIMO.")
else:
    print(f"El numero {numero} no es PRIMO.")
