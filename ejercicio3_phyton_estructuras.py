inventario = []

while True:
    print("\n===== MENU DE INVENTARIO =====")
    print("1. Agregar producto")
    print("2. Agregar lote de productos")
    print("3. Eliminar producto del inventario")
    print("4. Eliminar el producto mas reciente")
    print("5. Ordenar productos alfabeticamente")
    print("6. Mostrar numero total de productos")
    print("7. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        producto = input("Nombre del producto: ").strip()

        if producto:
            inventario.append(producto)
            print("Producto agregado.")
        else:
            print("Nombre no valido.")

    elif opcion == "2":
        try:
            cantidad = int(input("Cantidad de productos del lote: "))

            if cantidad <= 0:
                print("Ingrese una cantidad positiva.")
                continue

            for i in range(cantidad):
                producto = input(
                    "Nombre del producto " + str(i + 1) + ": "
                ).strip()

                if producto:
                    inventario.append(producto)
                else:
                    print("Producto vacio, no se agrego.")

            print("Lote procesado.")

        except ValueError:
            print("Debe ingresar un numero entero.")

    elif opcion == "3":
        producto = input("Producto que desea eliminar: ").strip()

        if producto in inventario:
            inventario.remove(producto)
            print("Producto eliminado.")
        else:
            print("El producto no existe en el inventario.")

    elif opcion == "4":
        if len(inventario) > 0:
            eliminado = inventario.pop()
            print("Producto retirado:", eliminado)
        else:
            print("El inventario esta vacio.")

    elif opcion == "5":
        inventario.sort(key=str.lower)
        print("Inventario ordenado:")
        for producto in inventario:
            print(producto)

    elif opcion == "6":
        print("Total de productos:", len(inventario))

    elif opcion == "7":
        print("Saliendo del programa.")
        break

    else:
        print("Opcion incorrecta.")