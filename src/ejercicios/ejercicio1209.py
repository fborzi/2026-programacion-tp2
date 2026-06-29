aprobados = 0
desaprobados = 0

cant = int(input("cuantas notas vas a cargar: "))

for i in range(cant):
    nota = int(input("ingrese nota: "))
    
    if nota > 4:
        aprobados = aprobados + 1
    else:
        desaprobados = desaprobados + 1
        
print("aprobados:", aprobados)
print("desaprobados:", desaprobados)        