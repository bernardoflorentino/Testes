import hashlib
import time

#cadastrar pessoa
def cadastrar_pessoa(nome,senha):
    with open("usuarios.txt","a") as arquivo:
        senha_bytes = str(senha).encode('utf-8')
        hash_senha = hashlib.sha256(senha_bytes).hexdigest()

        arquivo.write(f"{nome}:{hash_senha}\n")
        print("\n✅ Usuário cadastrado com sucesso! 🎉")
#verificar
def verificacao_senha_nome(senha_digitada,nome_digitado):
    try:
        senha_digitada_bytes = str(senha_digitada).encode('utf-8')
        hash_senha_digitada = hashlib.sha256(senha_digitada_bytes).hexdigest()

        with open("usuarios.txt","r") as arquivo:
            for linha in arquivo:
                nome_salvo, hash_salva =  linha.strip().split(':')
                if nome_salvo == nome_digitado and hash_salva == hash_senha_digitada:
                    return True
    except FileNotFoundError:
        return False
    return False

def main():
    print()
    while True:
        print("─" * 60)
        print("🏦💰      BEM-VINDO AO BANCO BRASIL BRASILEIRO      💰🏦")
        print("─" * 60)
        print("\n Opções: ")
        print("   [1] 📝  Cadastrar um novo usuário")
        print("   [2] 🔑  Fazer Login")
        print("   [3] 🚪  Sair do sistema")
        opcao = input("\n👉 Escolha uma opção: ")

        if opcao == None:
            print("Nenhuma escolha foi feita, tente novamente.")
        elif opcao == '1':
            nome=input("Entre com seu usuario: ")
            while True:
                try:
                    senha=(int(input("Cadatre uma senha: ")))
                    break
                except ValueError:
                    print("Deve conter somente numeros")
            cadastrar_pessoa(nome,senha)

        elif opcao == '2':
            nome=input("Insira seu usuario: ")
            while True:
                try:
                    senha=(int(input("Entre com sua senha: ")))
                    break
                except ValueError:
                    print("Deve conter somente numeros")
            if verificacao_senha_nome(senha,nome):
                print(f"Seja Bem Vindo,{nome}!")
                break
            else:
                print("Usuario ou senha incorreto...")


        elif opcao == '3':
            print("\n👋 Saindo do sistema.")
            time.sleep(1)
            print("👋 Saindo do sistema..")
            time.sleep(1)
            print("👋 Saindo do sistema...")
            time.sleep(1)
            print("\n Até logo!\n")
            break

if __name__ == "__main__":
    main()