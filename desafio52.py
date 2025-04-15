import random
import string

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''
    count = 0
    while count < tamanho:
        senha += random.choice(caracteres)
        count += 1
    return senha

while True:
    try:
        tamanho = int(input("Digite o tamanho da senha (ou 0 para sair): "))
        if tamanho == 0:
            break
        print("Senha gerada:", gerar_senha(tamanho))
    except ValueError:
        print("Digite um número válido.")
