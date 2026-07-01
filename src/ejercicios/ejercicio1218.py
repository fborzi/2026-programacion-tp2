"""Este programa solicita el ingreso del titulo de su libro preferido.imprimir luego 'Tu libro
preferido es:[nombre del libro ingresado]'donde el nombre del libro debe mostrarse con la primera letra en mayusucla
y el resto en minuscula independientemente de como el usuario lo haya ingresado,no es posible usar capitalize()."""


titulo_libro = input("Ingrese el titulo del libro: ")
titulo_libro = titulo_libro[0].upper() + titulo_libro[1:].lower()
print(f"Tu libro preferido es: {titulo_libro}")