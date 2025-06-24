tarefas = []

def mostrar_menu():
    print("\n--- Lista de Tarefas ---")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Remover tarefa")
    print("4. Sair")

def adicionar_tarefa():
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa.")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            print(f"{i}. {tarefa}")

def remover_tarefa():
    listar_tarefas()
    try:
        i = int(input("Número da tarefa a remover: ")) - 1
        if 0 <= i < len(tarefas):
            tarefas.pop(i)
            print("Tarefa removida!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        escolha = input("Escolha: ")
        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            listar_tarefas()
        elif escolha == "3":
            remover_tarefa()
        elif escolha == "4":
            break
        else:
            print("Opção inválida.")