aprobados = 0
desaprobados = 0
while True:
    legajo = int(input("ingresá el númer de alumno . 0 para terminar:"))
    if legajo == 0:
        break #corta el programa 
    nota = float(input(f"ingresá la nota del alumno {legajo}: "))
    if nota > 4:
        aprobados +=1
    else:
        desaprobados +=1
        print("/n----Resultados del final----")
        print(f"la cantidad de aprobados es: {aprobados}")
        print(f"la cantidad de desaprobados es: {desaprobados}")
       
       
        