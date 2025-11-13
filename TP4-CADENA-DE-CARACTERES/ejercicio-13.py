def numeros_a_letras(num: int):
    unidades = ["", "uno", "dos", "tres", "cuatro", "cinco",
                "seis", "siete", "ocho", "nueve"]
    decenas = ["", "diez", "veinte", "treinta", "cuarenta",
                "cincuenta", "sesenta", "setenta", "ochenta", 
                "noventa"]
    especiales = ["once", "doce", "trece", "catorce", "quince"]
    centenas = ["", "ciento", "doscientos", "trescientos",
                "cuatrocientos", "quinientos", "seiscientos",
                 "setecientos", "ochocientos", "novecientos"]

    grupos = ["", "mil", "millon", "mil millones", "billon"]
    resul = []
    if num == 0:
        return "cero"
    i = 0
    while num > 0:
        grupo = num % 1000
        num = num // 1000
        c = grupo // 100  
        d = (grupo % 100) // 10
        u = grupo % 10
        texto = ""

        if grupo == 100:
            texto = "cien"
        elif c > 0:
            texto += centenas[c] + " "
        if d == 1 and u > 0:
            texto += especiales[u - 1] + " "
        elif d > 1:
            texto += decenas[d]
            if u > 0:
                texto += " y " + unidades[u] + " "  
        else:
            if u > 0:
                texto += unidades[u] + " "
        texto = texto.strip()
        if texto:
            nombre = grupos[i]
            if nombre:
                if nombre == "millon" and grupo > 1:
                    nombre += "es"
                texto += " " + nombre
            resul.insert(0, texto)
        i += 1
    return " ".join(resul).strip()   

print(numeros_a_letras(123456789))
