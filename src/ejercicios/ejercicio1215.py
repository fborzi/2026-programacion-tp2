cadena = input("Ingrese una cadena de texto: ")
vocales = "aeiou" 
vocalesEncontradas = ""  

for letra in cadena:
    letraMinuscula = letra.lower()
    
    if letraMinuscula in vocales:
       
        if letraMinuscula not in vocalesEncontradas:
            vocalesEncontradas = vocalesEncontradas + " " + letraMinuscula

print("La cadena contiene las siguientes vocales:", vocalesEncontradas)