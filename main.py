def alunos_disciplina(vetor,aluno):
    aluno=int(input("Digite a quantidade de alunos na disciplina: "))
    vetor.append(aluno)
    return(aluno)

def calcular_medias(nota1,nota2,media,i):
    i=0
    media.append(nota1,nota2)
    sum(media)
    media//2
    print("A media do aluno%i"%i+1,"foi: %.2f"%media)
    return(media)

def media_disciplina(aluno,media,media_disciplina):
    media_disciplina = media / aluno
    print ("A média da disciplina foi de:%.2f"%media_disciplina) 
    
def media_materia(media_curso,media_disciplina,disciplinas,i):
    i=0
    media_curso=media_disciplina/disciplinas
    print("A média da máteria %i, foi de:%.2f"%i+1%media_curso)

def media_tecfa(media_curso,media_disciplina,i):
    print()

def main():
    vetor_curso=[]
    vetor_notas=[]
    vetor_alunos=[]
    curso = 1 
    i=0
    while curso <= 2:
        print("="*60)
        print("Bem vindo a faculdade tecfa!\n Vamos começar...")
        print("Curso",curso)
        disciplinas=int(input("Digite a quantidade total de disciplinas no curso %i"%curso+1,":"))
        vetor_curso.append(disciplinas)
        while disciplinas > i:
            aluno=int(input("Digite a quantidade de alunos na disciplina: "))
            alunos_disciplina(vetor_notas,aluno)
            print(aluno)
            while aluno > i:
                print("Aluno%i"%i+1)
                nota1 = float(input("Digite a nota 1: "))
                nota2 = float(input("Digite a nota 2: "))
                calcular_medias(nota1,nota2)
                print(calcular_medias)

if __name__ == "___main___":
    main()
