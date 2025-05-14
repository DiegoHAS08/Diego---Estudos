import random

print("Jogo do Par ou Ímpar")
vitorias = 0

while True:
    jogador = int(input("Digite um número: "))
    escolha = input("Par ou Ímpar? [P/I] ").strip().upper()
    computador = random.randint(0, 10)
    total = jogador + computador

    print(f"Você jogou {jogador} e o computador {computador}. Total = {total}")

    if (total % 2 == 0 and escolha == 'P') or (total % 2 == 1 and escolha == 'I'):
        print("Você VENCEU!")
        vitorias += 1
    else:
        print("Você PERDEU!")
        break

print(f"Fim de jogo! Você venceu {vitorias} vez(es).")
