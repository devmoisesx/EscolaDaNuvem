n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))
operacao = input("Escolha uma operacao (+, -, * ou /): ")

match operacao:
    case "+":
        print(f"Resultado da conta: {n1 + n2}")
    case "-":
        print(f"Resultado da conta: {n1 - n2}")
    case "*":
        print(f"Resultado da conta: {n1 * n2}")
    case "/":
        print(f"Resultado da conta: {n1 / n2}")
