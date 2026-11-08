def superReducedString(s):
    resultado = []

    for letra in s:
        if len(resultado) > 0 and resultado[-1] == letra:
            resultado.pop()
        else:
            resultado.append(letra)

    if len(resultado) == 0:
        return "Empty String"
    else:
        return "".join(resultado)


s = input("Ingrese una cadena: ")
respuesta = superReducedString(s)

print(respuesta)