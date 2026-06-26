anterior = 0
numero = 1
contador = 0

while contador < 25:
    print(anterior) 
    siguiente = numero + anterior
    anterior =  numero
    numero = siguiente
    contador = contador +1 