def mayor_unico(a: int, b: int, c: int) -> int:
    """
    Recibe 3 nuumeros enteros y devuelve el mayor.
    Siempre y cuando sea repetido.
    
    Pre: los argumentos deben ser numeros enteros
    
    post: Retorna el numero mayor si es unico, caso contrario devuelve -1
    """
    if a > b: #Este bloque es para evaluar a
        if a > c:
            if a == b:
                return -1
            if a == c:
                return -1
            return a
    
    elif b > a:
        if b > c:
            if b == a:
                return -1
            if b == c:
                return -1
            return b

    elif c > a:
        if c > b:
            if c == a:
                return -1
            if c == b:
                return -1
            return c
    return -1


num1 = int(input("Ingrese primero numero: "))
num2 = int(input("Ingrese segundo numero: "))
num3 = int(input("Ingrese tercer numero: "))
funcion = mayor_unico(num1, num2, num3)
if funcion != -1:
    print(f"El maximo hallado es {funcion}")
else:
    print("valor unico no existente")


