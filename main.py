nombreVendedor=None 
productos=[]
producto={}

opcion=100

print("Mercado")
print("********")
print("1. Crear lista mercado")
print("2. Ver Lista de mercado")
print("3. Editar producto de la lista")
print("4. Retirar producto de la lista")
print("Presiona 5 para salir")
while opcion != 5:
    opcion=int(input("Digita una opcion: "))
    if opcion == 1:
        print("Bienvenido a la creacion de tu lista de mercado")
        
        #creando claves y valores de un diccionario
        producto["id"]=5
        producto["nombre"]=input("Digita el nombre del producto: ")
        producto["precio"]=int(input("Digita el precio del producto: "))
        producto["cantidad"]=int(input("Cuantos elementos de este producto vas a llevar: "))
        producto["presentacion"]=input("Cual presentacion llevaras? ")
        
        #mostrando mi diccionario
        #print(producto)
        
        #poblando una lista (agrgando elementos a una lista)
        productos.append(producto)
        print(productos)
        
        
        
    elif opcion==2:

        "utilizando ciclo for en python para recorrer listas 11032025"
        for producto in productos:
            print(producto["nombre"])
    elif opcion==3:
        print("estoy en la 3")
        #modificar un producto
        #0. PREGUNTAR A QUIEN QUIERO EDITAR
        productoCambio=int(input("Digite el ID del producto a cambiar:"))
        #1. ENCONTRAR EL ELEMENTO
        for productoBuscado in productos:
            if productoBuscado["id"]==productoCambio:
                print("Producto encontrado")
            else:
                print("Producto no encontrado")
                #2. MODIFICO LOS VALORES
                productoBuscado["nombre"]=input("Digita el nuevo nombre del producto: ")
                productoBuscado["precio"]=int(input("Digita el nuevo precio del producto: "))
                productoBuscado["cantidad"]=int(input("Cuantos elementos de este producto vas a llevar: "))
                productoBuscado["presentacion"]=input("Cual presentacion llevaras? ")
                print("Producto modificado correctamente")
                break
        #2. SELECCIONO EL ELEMENTO 
        #3. ACCEDO A LSA PROPIEDADES O ATRIBUTOS QUE QUIERO O PUEDO MODIFICAR
    elif opcion==4:
        print("estoy en la 4")
    else:
        print("Opcion no valida")
        