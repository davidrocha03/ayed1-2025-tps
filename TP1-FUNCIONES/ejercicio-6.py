def concatenar_numeros(a: int, b: int) ->int:
    """
    La funcion devolvera los 2 parametros que se ingresaron concatenados 
    siempre y cuando sean enteros positivos
    
    Pre: los parametros a y b deben ser numeros enteros positivos

    Post: la funcion devolvera un unico numero entero que es la concatenacion de a y b


    """

    contador = 0
    if b == 0:
        contador += 1
    else:
        temp = b
        while temp > 0:
            temp //= 10
            contador += 1
    multi = 1
    for i in range(contador):
        multi *= 10
    return a * multi + b

try:
    num1 = int(input("Ingresa primero numero positivo: "))
    num2 = int(input("Ingresa segundo numero positivo: "))
    if num1 >= 0 and num2 >= 0:
        resul = concatenar_numeros(num1, num2)
        print(f"Resultado concatenado es: {resul}")
    else:
        print("Ambos numeros deben ser positivos")
except ValueError:
    print("Invalido. Ingrese numeros enteros positivos")

