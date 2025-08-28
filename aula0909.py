import array

def adicionar_veiculo(nomes, anos, nome, ano):
    nomes.fromunicode(nome + '\0')
    anos.append(ano)
    print("Veiculo:",nome)
    print("Ano:",ano)

def listar_veiculos(nomes,anos):
    nomes_str= nomes.tounicode().split('\0')
    if nomes_str[0]:
        print("Veículos cadastrados")
        for i in range(len(anos)):
            print("Nome: ",nomes_str[i])
            print("Ano",anos[i])
    else:
        print("Nenhum veículo cadastrados")

def remover_veiculo(nomes, anos, nome):
    nomes_str = nomes.tounicode().split('\0')
    if nome in nomes_str:
        indice = nomes_str.index(nome)
        del nomes_str[indice]
        anos.pop(indice)
        print("Veículo removido")
    else:
        print("Veículo não cadastrado")

def main():
    nomes_veiculos = array.array('u')
    anos_veiculos = array.array('i')
    
    while True:
        print("Digite 1 para cadastrar um veículo")
        print("Digite 2 para remover um veículo")
        print("Digite 3 para sair")
        print()
        opcao=input("Entre com uma opção: ")

        if opcao == '1':
            nome = input("Digite o nome do veículo: ")
            ano = int(input("Digite o ano do veículo: "))
            adicionar_veiculo(nomes_veiculos,anos_veiculos,nome,ano)
        if opcao == '2':
            nome = input("Digite o nome do veículo a ser removido: ")
            remover_veiculo(nomes_veiculos,anos_veiculos,nome)
        if opcao == '3':
            print("Saindo...")
            break

if __name__ == '__main__':
    main()