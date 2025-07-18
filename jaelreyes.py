

#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video], ...]
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}

#stock = {modelo: [precio, stock], ...]
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0], 
}

#OPCION1 
def stock_marca(marca):
    marca=marca.lower()
    total_stock=0

    for modelo, datos in productos.items():
        if datos[0].lower() == marca:
            total_stock += stock[modelo][1]
            

    if total_stock > 0:
        print(f"Stock total de la marca {marca}: {total_stock} unidades.")
    else:
        print(f"No se encuentra stock disponible de la marca {marca}")

            

#OPCION2
def busqueda_precio(p_min, p_max):
    productos_encontrados=[]

    for modelo,(precio, cantidad) in stock.items():
        if cantidad > 0 and p_min <= precio <= p_max:
            marca = productos[modelo][0]
            productos_encontrados.append(f"{marca} -- {modelo}")
    if productos_encontrados:
        productos_encontrados.sort()
        print("Productos encontrados:")
        for producto in productos_encontrados:
            print(producto)
    
    else:
        print("No hay notebooks en ese rango de precios.")


#OPCION 3
def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        return True
    else:
        return False


#menu
def menu():
    while True:
        print("\n***MENU PRINCIPAL***")
        print("1. Stock marca")
        print("2. Busqueda por precio")
        print("3. Actualizar precio")
        print("4. Salir")

        try:
            opcion=int(input("Ingrese opcion(1-4): "))
        except ValueError:
            print("Error: Opcion es un numero entero del 1 al 4.")
            continue
      
        if opcion == 1:
            marca_ingresada=(input("Ingrese marca a consultar: "))
            stock_marca(marca_ingresada)

        elif opcion == 2:
            while True:
                try:
                    precio_minimo=int(input("Ingrese precio minimo: "))
                    precio_maximo=int(input("Ingrese precio maximo: "))
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!!")
            busqueda_precio(precio_minimo, precio_maximo)

        elif opcion == 3:
            while True:
                modelo=input("Ingrese codigo del modelo a actualizar: ").upper()

                try:
                    precio=int(input("Ingrese precio nuevo: "))
                except ValueError:
                    print("Error: Precio es un numero entero.")
                    continue

                if actualizar_precio(modelo, precio):
                    print("Precio actualizado!!!")


                else:
                    print("El modelo no existe!!!")

                if input("¿Desea actualizar otro precio? (s/n)?: ").lower() == "no":
                    break
                 

        elif opcion == 4:
            print("Programa finalizado.")
            break

        else:
            print("Debe seleccionar una opción valida!!!")

menu()