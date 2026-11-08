def solution(a):
    equipo1 = 0
    equipo2 = 0

    for i in range(len(a)):
        if i % 2 == 0:
            equipo1 += a[i]
        else:
            equipo2 += a[i]

    return [equipo1, equipo2]


pesos = []

cantidad = int(input("Ingrese la cantidad de personas: "))

for i in range(cantidad):
    peso = int(input("Peso de la persona " + str(i + 1) + ": "))
    pesos.append(peso)

resultado = solution(pesos)

print("Peso total del equipo 1:", resultado[0])
print("Peso total del equipo 2:", resultado[1])
print("Resultado:", resultado)