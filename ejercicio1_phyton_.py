dias = ["Lunes", "Martes", "Miercoles", "Jueves",
        "Viernes", "Sabado", "Domingo"]

ventas = []
precios = []

print("VENTAS DE LA SEMANA")

for i in range(5):
    fila = []
    print("Producto", i + 1)

    for j in range(7):
        cantidad = int(input(dias[j] + ": "))
        fila.append(cantidad)

    ventas.append(fila)

print("\nPRECIOS DE LOS PRODUCTOS")

for i in range(5):
    precio = float(input("Precio del producto " + str(i + 1) + ": "))
    precios.append(precio)

# Calcular ingresos por producto
ingresos_productos = []

for i in range(5):
    total = 0

    for j in range(7):
        total = total + ventas[i][j] * precios[i]

    ingresos_productos.append(total)

# Calcular ingresos por dia
ingresos_dias = []

for j in range(7):
    total = 0

    for i in range(5):
        total = total + ventas[i][j] * precios[i]

    ingresos_dias.append(total)

# Buscar producto con mayores ingresos
mayor_producto = 0

for i in range(5):
    if ingresos_productos[i] > ingresos_productos[mayor_producto]:
        mayor_producto = i

# Buscar dia con mayores ingresos
mayor_dia = 0

for j in range(7):
    if ingresos_dias[j] > ingresos_dias[mayor_dia]:
        mayor_dia = j

print("\nRESULTADOS")
print("Producto con mayores ingresos:",
      mayor_producto + 1)

print("Ingresos:", ingresos_productos[mayor_producto])

print("Dia con mayores ingresos:", dias[mayor_dia])

print("Ingresos:", ingresos_dias[mayor_dia])