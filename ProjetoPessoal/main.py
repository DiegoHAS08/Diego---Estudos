import sys
import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"Tarefa adicionada: {description}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return
    for i, task in enumerate(tasks, 1):
        status = "✔️" if task["done"] else "❌"
        print(f"{i}. [{status}] {task['description']}")

def mark_done(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"Tarefa {index} marcada como concluída.")
    else:
        print("Índice inválido.")

def remove_task(index):
    tasks = load_tasks()
    if 0 < index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Tarefa removida: {removed['description']}")
    else:
        print("Índice inválido.")

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py [add|list|done|remove] ...")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Uso: python main.py add \"descrição da tarefa\"")
        else:
            description = " ".join(sys.argv[2:])
            add_task(description)

    elif command == "list":
        list_tasks()

    elif command == "done":
        if len(sys.argv) != 3 or not sys.argv[2].isdigit():
            print("Uso: python main.py done <número da tarefa>")
        else:
            mark_done(int(sys.argv[2]))

    elif command == "remove":
        if len(sys.argv) != 3 or not sys.argv[2].isdigit():
            print("Uso: python main.py remove <número da tarefa>")
        else:
            remove_task(int(sys.argv[2]))

    else:
        print(f"Comando desconhecido: {command}")

if __name__ == "__main__":
    main()
