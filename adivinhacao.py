# adivinhacao.py
import random

def jogo_adivinhacao():
    print("=== Jogo da Adivinhação ===")
    dificuldade = input("Escolha a dificuldade (fácil / médio / difícil): ").lower()

    if dificuldade == "fácil":
        tentativas = 10
        numero_secreto = random.randint(1, 50)
    elif dificuldade == "médio":
        tentativas = 7
        numero_secreto = random.randint(1, 100)
    elif dificuldade == "difícil":
        tentativas = 5
        numero_secreto = random.randint(1, 200)
    else:
        print("Dificuldade inválida.")
        return

    while tentativas > 0:
        try:
            chute = int(input("Digite seu palpite: "))
        except ValueError:
            print("Digite um número válido.")
            continue

        if chute == numero_secreto:
            print("Parabéns! Você acertou!")
            return
        elif chute < numero_secreto:
            print("Muito baixo!")
        else:
            print("Muito alto!")

        tentativas -= 1
        print(f"Tentativas restantes: {tentativas}")

    print(f"Fim de jogo! O número era {numero_secreto}")

if __name__ == "__main__":
    jogo_adivinhacao()
