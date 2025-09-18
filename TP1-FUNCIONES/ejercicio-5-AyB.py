def es_oblongo(n: int)-> bool:
    """
    La funcion verifica si un numero entero es un oblongo

    Pre: el parametro que ingresa debe ser un entero positivo

    Post: la funcion devuelve True si es oblongo, caso contrario devuelve False
    """
    for i in range(1, n):
        if i *(i + 1) == n:
            return True 
  
    return False

while True:
    fun = int(input("INgrese numero (0 Para salir): "))
    if fun >= 1:
        resul = es_oblongo(fun)
        print(resul)
    elif fun == 0:
        break

# Hasta aqui verifica si es un numero oblongo en una funcion
#---------------------------------

# Numero oblongo con funcion lambda ejercicio A

es_n_oblongo = lambda n: any(i * (i +1) == n for i in range(1, n))
print(es_n_oblongo(8))

# Numero triangular con funcion lambda ejercicio B

es_triangular = lambda n: any(sum(range(1, i + 1)) == n for i in range(1, n))
print(es_triangular(8))