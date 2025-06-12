#ejercicio8
stock_productos = {}
while True:
    opcion = input("opción (consultar/agregar/salir): ")
    if opcion == "salir":
        break
    producto = input("producto: ")
    if opcion == "consultar":
        print("stock:", stock_productos.get(producto, "no existe"))
    elif opcion == "agregar":
        cantidad = int(input("cantidad: "))
        if producto in stock_productos:
            stock_productos[producto] += cantidad
        else:
            stock_productos[producto] = cantidad
