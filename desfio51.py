def eh_primo(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# Loop para verificar vários números
while True:
    entrada = input("Digite um número para verificar se é primo (ou 'sair'): ")
    if entrada == 'sair':
        break
    if entrada.isdigit():
        numero = int(entrada)
        print(f"{numero} é primo? {eh_primo(numero)}")
    else:
        print("Por favor, digite um número válido.")
