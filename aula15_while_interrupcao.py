# Exemplo didático de interrupção com while
while True:
    nome = input("Digite seu nome (ou 'sair' para encerrar): ")
    if nome.lower() == "sair":
        break
    print(f"Olá, {nome}!")