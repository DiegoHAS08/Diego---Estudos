def menu():
    print("\n=== MENU DE OPÇÕES ===")
    print("1. Progressão Aritmética")
    print("2. Sequência de Fibonacci")
    print("3. Sair")

def progressao_aritmetica():
    print("\n--- Progressão Aritmética ---")
    primeiro = int(input("Digite o primeiro termo: "))
    razao = int(input("Digite a razão: "))
    termos = int(input("Quantos termos você quer mostrar? "))
    
    count = 1
    atual = primeiro
    while count <= termos:
        print(atual, end=" → ")
        atual += razao
        count += 1
    print("FIM")

def sequencia_fibonacci():
    print("\n--- Sequência de Fibonacci ---")
    termos = int(input("Quantos termos você quer mostrar? "))
    
    a, b = 0, 1
    count = 0
    while count < termos:
        print(a, end=" → ")
        a, b = b, a + b
        count += 1
    print("FIM")

# Programa principal
while True:
    menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        progressao_aritmetica()
    elif opcao == "2":
        sequencia_fibonacci()
    elif opcao == "3":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
