import json
import os

# Caminho do arquivo de dados
ARQUIVO = "tarefas.json"

# Carregar tarefas do arquivo

def carregar_tarefas():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

# Salvar tarefas no arquivo
def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

# Listar tarefas
def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    print("\n=== Suas Tarefas ===")
    for i, t in enumerate(tarefas, 1):
        status = "✔️" if t["concluida"] else "❌"
        print(f"{i}. {t['titulo']} - {status}")

# Adicionar tarefa
def adicionar_tarefa(tarefas):
    titulo = input("Digite o título da tarefa: ").strip()
    if titulo:
        tarefas.append({"titulo": titulo, "concluida": False})
        salvar_tarefas(tarefas)
        print("Tarefa adicionada com sucesso!")
    else:
        print("Título inválido!")

# Concluir tarefa
def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa concluída: ")) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa concluída!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Entrada inválida!")

# Excluir tarefa
def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa a excluir: ")) - 1
        if 0 <= indice < len(tarefas):
            removida = tarefas.pop(indice)
            salvar_tarefas(tarefas)
            print(f"Tarefa '{removida['titulo']}' excluída!")
        else:
            print("Número inválido!")
    except ValueError:
        print("Entrada inválida!")

# Menu principal
def menu():
    tarefas = carregar_tarefas()
    while True:
        print("\n=== GERENCIADOR DE TAREFAS ===")
        print("1 - Listar tarefas")
        print("2 - Adicionar tarefa")
        print("3 - Concluir tarefa")
        print("4 - Excluir tarefa")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            concluir_tarefa(tarefas)
        elif opcao == "4":
            excluir_tarefa(tarefas)
        elif opcao == "0":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()
