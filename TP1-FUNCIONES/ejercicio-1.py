def mayor_unico(a: int, b: int, c: int) -> int:
    """
    Recibe 3 numeros positivos y devuelve el mayor
    Siempre y cuando sea unico

    Pre: Los argumentos deben ser numero enteros
    
    Post: Retorna el mayor de ellos siempre y cuando sa unico, caso contrario retorna -1 
    
    """
    if a > b:
        if a > c:
            return a
        
    if b > a:
        if b > c:
            return b
    
    if c > a:
        if c > b:
            return c
    
    return -1

a = int(input("INgresa Num 1: "))
b = int(input("INgresa NUm2: "))
c = int(input("Ingresa NUm3: "))
funcion = mayor_unico(a, b, c)
print(funcion)