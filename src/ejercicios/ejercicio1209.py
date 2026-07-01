"""
Lee alumno y nota hasta ingresar alumno 0; cuenta aprobados y desaprobados.
"""
aprobados = 0
desaprobados = 0

while True:
    numero_alumno = int(input("Ingrese el número de alumno (0 para finalizar): "))
    if numero_alumno == 0:
        break
    nota = float(input("Ingrese la nota: "))
    if nota > 4:
        aprobados += 1
    else:
        desaprobados += 1

print(f"La cantidad de aprobados es: {aprobados}")
print(f"La cantidad de desaprobados es: {desaprobados}")