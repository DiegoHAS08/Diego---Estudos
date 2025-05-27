# Exercício 84 - Lista composta e análise de dados

galera = []
dado = []
totmaior = totmenor = 0

for i in range(3):
    dado.append(input("Nome: "))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} é maior de idade.")
        totmaior += 1
    else:
        print(f"{p[0]} é menor de idade.")
        totmenor += 1

print(f"Total de maiores de idade: {totmaior}")
print(f"Total de menores de idade: {totmenor}")
