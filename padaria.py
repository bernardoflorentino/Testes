def adicionar_produtos(lista,nome,quantidade,validade,producao):
    produto = {
        "nome": nome,
        "quantidade": quantidade,
        "validade": validade,
        "producao": producao
    }
    lista.append(produto)
    print("Produto:",nome)
    print("Quantidade:",quantidade)
    print("Produção:",producao)
    print("Validade:",validade)
    

def remover_produto(lista,nome):
    for produto in lista:
        if produto["nome"] == nome:
            lista.remove(produto)
            print("Produto removido:",nome)
            return
        print("Produto não encontrado no sistema")

def remover_quantidade(lista,nome,quantidade):
    for produto in lista:
        if produto ["nome"] == nome:
            num_remove=int(input("Digite a quantidade a ser removida"))
            quantidade_nova=num_remove-quantidade
            print(quantidade_nova)



def listar_produtos(lista):
    if lista:
        print("Produtos cadastrados")
        for produto in lista:
            print("Nome:",{produto["nome"]})
            print("Quantidade:",{produto["quantidade"]})
            print("Produção:",{produto["producao"]})
            print("Validade:",{produto["validade"]})
    else:
        print("Produto não encontrado no sistema")

def main():
    lista_produtos=[]
    while True:
        print("PADARIA")
        print("="*60)
        print("Digite 1 para cadastrar um novo produto")
        print("Digite 2 para remover um produto")
        print("Digite 3 para listar os produtos")
        print("Digite 4 para sair")
        print("="*60)
        opcao=input("Entre: ")
        if opcao == '1':
            print("="*60)
            nome = input("Digite o nome do produto: ")
            quantidade = input("Digite a quantidade de produtos: ")
            producao = input("Digite a data de produção: ")
            validade = input("Digite a a data de validade: ")
            print("="*60)
            adicionar_produtos(lista_produtos,nome,quantidade,producao,validade,)
            print("="*60)
            print("Produto cadastrado!")
            print("="*60)
        elif opcao == '2':
            nome = input("Digite o nome do produto a ser removido: ")
            print("="*60)
            remover_produto(lista_produtos,nome)
            print("Produto removido com sucesso!")
            print("="*60)
        elif opcao == '3':
            print("="*60)
            listar_produtos(lista_produtos)
            print("="*60)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção invalida. Tente novamente")

if __name__ == "__main__":
    main()