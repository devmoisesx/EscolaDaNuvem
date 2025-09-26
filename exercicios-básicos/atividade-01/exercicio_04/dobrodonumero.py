def dobra_numero():
    x = int(input())
    if type(x) is not int:
        return print("Dado inserido inválido. Apenas números")
    return print(x * 2)


dobra_numero()
