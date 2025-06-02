fator_gravitacional = {
    "mercurio": 0.38,
    "venus": 0.90,
    "terra": 1.00,
    "marte": 0.38,
    "jupiter": 2.34,
    "saturno": 1.06,
    "urano": 0.92,
    "netuno": 1.14
}

while True:
    planeta = input(f'\nInfome em qual planeta está: ').lower()
    meu_peso = float(input(f'Informe seu peso atual: '))

    match planeta:
        case "terra":
            print(f"Seu pesso na Terra é {meu_peso}")
        case i if i in fator_gravitacional:
            print(f"Seu peso em {planeta} é {meu_peso * fator_gravitacional[i]}")
        case _:
            print("Planeta não encontrado!")