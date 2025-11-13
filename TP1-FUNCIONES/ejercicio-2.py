def fecha_valida(dia: int, mes: int, anio: int) -> bool:
    """
    Esta funcion verifica si el dia, mes y año son validos y si el año es bisiesto o no.
    
    Pre: Los datos ingresados deben ser numeros enteros 

    Post: Retorna True si la fecha el correcta caso contrario retorna False 

    """

    if mes in (1, 3, 5, 7, 8,10,12): # aqui estan los meses con 31 dias
        if dia <= 31:
            return True 
         
    elif mes in (4,6,9,11): # En esta lista estan los meses de 30 dias 
        if dia <= 30:
            return True
        
    elif mes == 2:
        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            if dia <= 29:
                return True
        else:
            if dia <= 28:
                return True 
    else:
        return False
            
    

while True:
    dia = int(input("Ingresa el dia: "))
    if dia > 0 and dia <= 31:
        break
while True:
    mes = int(input("Ingrese el mes: "))
    if mes >= 1 and mes <= 12:
        break
while True:
    anio = int(input("Ingresa el año: "))
    if anio > 0 and anio <= 2500:
        break
if fecha_valida(dia, mes, anio):
    print('La fecha es valida')
else: 
    print('Fecha invalida')


