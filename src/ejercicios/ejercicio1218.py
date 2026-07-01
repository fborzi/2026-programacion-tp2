libro=input("Ingresa el nombre del libro:")
fraseNueva=""

for letra in libro :
    if fraseNueva == "" :
        fraseNueva= fraseNueva +letra.upper()
    else :
       fraseNueva= fraseNueva +letra.lower()
print("El nombre del libro es:", fraseNueva)