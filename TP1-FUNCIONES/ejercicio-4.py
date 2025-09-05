# Librería RE
import re

# @title Método MATCH

cadenas = ["A123E", "B456", "C789", "123A", "D3214"]
# una letra mayúscula o minúscula y 3 números del 1 al 3
patron = "[A-Za-z][1-3]{3}$"

#Iteramos sobre las cadenas​

for cadena in cadenas:
    if re.match(patron, cadena): # retorna un objeto match, no retorna bool
        print(f"La cadena {cadena} coincide con el patrón.")
    else:
        print(f"La cadena {cadena} no coincide con el patrón.")