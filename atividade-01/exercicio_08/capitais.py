capitais = {
    "Brasil": "Brasília",
    "Estados Unidos": "Washington",
    "França": "Paris",
    "Itália": "Roma",
}

for i in capitais.keys():
    print(i)

escolha = input("Escolha um país da lista: ")

match escolha:
    case "Brasil":
        print(capitais.get("Brasil"))
    case "Estados Unidos":
        print(capitais.get("Estados Unidos"))
    case "França":
        print(capitais.get("França"))
    case "Itália":
        print(capitais.get("Itália"))
