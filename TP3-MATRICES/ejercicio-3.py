import random as rn 


def matriz_aleatoria():
    """
    La funcion carga una matriz con numeros enteros de forma aleatoria [0,N**2]

    Pre: Los numeros deben ser elevados al cuadrado de manera aleatoria 
    Post: Retorna una matriz cargada con numeros enteros positivos al cuadrado
    """
    matriz = []
    n = 3
    numeros = rn.sample(range(0, n**2),n**2)
    print(numeros)
    
    for i in range(n):
        fila = numeros[i*n : (i+1)*n]
        matriz.append(fila)
    return matriz


l = matriz_aleatoria()
for i in l:
    print(i)
