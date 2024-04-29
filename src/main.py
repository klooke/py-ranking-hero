print("\nBem vindo ao Classificador de heroi:")

def get_level(exp):
    if exp <= 1000:
        return "Ferro"
    elif exp <= 2000:
        return "Bronze"
    elif exp <= 5000:
        return "Prata"
    elif exp <= 7000:
        return "Ouro"
    elif exp <= 8000:
        return "Platina"
    elif exp <= 9000:
        return "Ascendente"
    elif exp <= 10000:
        return "Imortal"
    else:
        return "Radiante"


while (True):
    print("\nCrie um herói digitando seu nome e o XP: (deixe vazio para sair)\n")

    try:
        nome = input("-Nome:")
        if nome == "": break

        exp = int(input("-XP:"))
    except (ValueError, EOFError):
        break

    print(f"\nO Herói de nome {nome} está no nível de {get_level(exp)}")
