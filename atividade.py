import re

def verificar_senha(senha):
    erros = []

    if len(senha) < 8:
        erros.append("A senha deve ter pelo menos 8 caracteres.")
    if not re.search(r"[A-Z]", senha):
        erros.append("A senha deve conter pelo menos uma letra maiúscula.")
    if not re.search(r"[a-z]", senha):
        erros.append("A senha deve conter pelo menos uma letra minúscula.")
    if not re.search(r"[0-9]", senha):
        erros.append("A senha deve conter pelo menos um número.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        erros.append("A senha deve conter pelo menos um caractere especial.")

    if erros:
        print("\n❌ Senha inválida pelos seguintes motivos:")
        for erro in erros:
            print(f"- {erro}")
    else:
        print("✅ Senha válida!")

def menu():
    print("===== Validador de Senhas =====")
    print("Digite uma senha para validar ou 'sair' para encerrar.")

    while True:
        senha = input("\nDigite a senha: ")
        if senha.lower() == "sair":
            print("Encerrando programa. Até mais!")
            break
        verificar_senha(senha)

if __name__ == "__main__":
    menu()
