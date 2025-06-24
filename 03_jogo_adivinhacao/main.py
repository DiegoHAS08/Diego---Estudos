import random

def jogo():
    print("Bem-vindo ao Jogo de Adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Digite um número entre 1 e 100: "))
            tentativas += 1
            if palpite < numero_secreto:
                print("Muito baixo.")
            elif palpite > numero_secreto:
                print("Muito alto.")
            else:
                print(f"Parabéns! Você acertou em {tentativas} tentativas.")
                break
        except ValueError:
            print("Digite um número válido.")

if __name__ == "__main__":
    jogo()