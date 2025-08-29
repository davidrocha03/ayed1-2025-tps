"""
def doble(x):
    return x * 2

resul = doble(5) 
print(resul) 
"""

def map_(Lista: list[int]) -> list[int]:
    lista2 = []
    return list(map( lambda x: x * 2, lista))

lista = [1,2,3,4,5]
resultado = map_(lista)
print(resultado)
#"""

