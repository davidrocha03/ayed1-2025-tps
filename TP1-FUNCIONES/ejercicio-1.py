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
        elif a == c:
            return -1
        
    if b > a:
        if b > c:
            return b
        elif b == a:
            return -1
    
    if c > a:
        if c > b:
            return c
        elif c == b:
            return -1
    
    return -1

while True:
    a = int(input("Ingrese A: "))
    break
while True:
    b = int(input("Ingrese B: "))
    break
while True:
    c = int(input("Ingrese c: "))
    break

resul = mayor_unico(a,b,c)
if resul > -1:
    print(f"El mayor es {resul}")
else:
    print("No hay números unicos")