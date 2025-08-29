def menu_opciones():
    opcion = ''
    print("--- MENU DE OPCIONES ---")
    print("1. Informa la cantidad de productos según su categoria")
    print("2. Para modificar producto y precio")
    print("3. Informar precio y promedio según la categoria")
    print("4. Informar nombre del producto con menor stock")
    print("5. Informar el nombre del procuducto mas csato")
    print("1. Salir")
    opcion = input("Ingrese la opcion: ")      
    while opcion != '0':
        opcion = input("Ingrese la opcion deseada: ")
        if opcion == '1':
            #llama funcion
        elif opcion == '2':
