n = int(input("Ingrese el tamaño de la matriz cuadrada: "))

if n <= 0:
    print("El tamaño debe ser positivo.")
else:
    matrices = [[] for i in range(8)]

    for i in range(n):
        filas = [[] for k in range(8)]

        for j in range(n):
            # Matriz 1: numeros consecutivos por filas
            filas[0].append(i * n + j + 1)

            # Matriz 2: filas alternadas
            if i % 2 == 0:
                filas[1].append(j + 1)
            else:
                filas[1].append(n - j)

            # Matriz 3: diagonal principal
            filas[2].append(1 if i == j else 0)

            # Matriz 4: diagonal secundaria
            filas[3].append(1 if i + j == n - 1 else 0)

            # Matriz 5: triangulo inferior
            filas[4].append(1 if j <= i else 0)

            # Matriz 6: triangulo superior
            filas[5].append(1 if j >= i else 0)

            # Matriz 7: numeros consecutivos por columnas
            filas[6].append(j * n + i + 1)

            # Matriz 8: triangulo de letras A y B
            if j <= i:
                filas[7].append("A" if j % 2 == 0 else "B")
            else:
                filas[7].append(" ")

        for k in range(8):
            matrices[k].append(filas[k])

    nombres = [
        "Matriz 1: Numeros por filas",
        "Matriz 2: Filas alternadas",
        "Matriz 3: Diagonal principal",
        "Matriz 4: Diagonal secundaria",
        "Matriz 5: Triangulo inferior",
        "Matriz 6: Triangulo superior",
        "Matriz 7: Numeros por columnas",
        "Matriz 8: Letras A y B"
    ]

    for k in range(8):
        print("\n" + nombres[k])

        for fila in matrices[k]:
            print(" ".join(f"{valor:>3}" for valor in fila))