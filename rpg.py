def criar_personagem(vetor,nome,vida,mana,dano,exp):
    personagem = {
        "nome": nome,
        "vida": vida,
        "mana": mana,
        "dano": dano,
        "exp": exp
    }
    vetor.append(personagem)
    print("Personagem criado com sucesso!")
    print("Seus atributos:")
    print(personagem)

def listar_personagens(vetor):
    if personagem:
        for personagem in vetor:
            print(vetor)
    else:
        print("Nenhum personagem foi criado.")

def criar_monstro(vetor2,nome,vida,mana,dano,exp):
    monstro = {
        "nome": nome,
        "vida": vida,
        "mana": mana,
        "dano": dano,
        "exp": exp
    }
    vetor2.append(monstro)
    print(monstro)

def level_up(personagem,exp,nome):
    exp = 0
    level = 1
    if personagem ["nome"] == nome:
        if exp > 100:
            print("Personagem evoluiu para o Level%i"%level+1)

def main():
    print()
    

