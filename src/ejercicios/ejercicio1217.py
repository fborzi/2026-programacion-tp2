string_completo = ""

while True:
    caracter = input()
    if len (caracter) != 1:
        break
    
    if caracter == "0":
        break
    
    string_completo = string_completo + caracter
    
print(string_completo)