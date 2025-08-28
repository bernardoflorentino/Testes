import array
#importando array

def adicionar_numeros(vetor,numero):
    vetor.append(numero)
    print("Número adicionado:",numero)
#adicionando um numero do array

def remover_numeros(vetor,numero):
    numero=float(input("Digite o número a ser removido: "))
    if numero in vetor:
        numero.remove
        print("Número removido:",numero)
#removendo um numero do array

def listar_numeros(vetor):
    if vetor:
        print("Números no array")
        for num in vetor:
            print("\nElementos",num)
        else:
            print("Array está vazio.")
#listando numeros do array

def somar_numeros(vetor):
    total = sum(vetor)
    print(total)
#somando todos os numeros do array

def main():
    #criando o array
    vetor_numeros= array.array('f') #--> definindo o tipo do array


    while True:
        print("Digite 1 para Adicionar")
        print("Digite 2 para Remover")
        print("Digite 3 para Listar")
        print("Digite 4 para Somar")
        print("Digite 5 para Sair")
        print()
        opcao=input("Escolha uma opção: ")
        if opcao == '1':
            numero = float(input("Entre com um número: "))
            adicionar_numeros(vetor_numeros,numero)
        elif opcao == '2':
            numero = float(input("Entre com um número a ser removido: "))
            remover_numeros(vetor_numeros,numero)
        elif opcao == '3':
            listar_numeros(vetor_numeros)
        elif opcao == '4':
            somar_numeros(vetor_numeros)
        elif opcao == '5':
            break
        else:
            print("Opção Invalida. Tente novamente")

if __name__ == "__main__":
    main()