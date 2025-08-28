from time import sleep

#Tabuada---------------------------------------------------------------
def tabuada(num,x):
    for x in range(10):
        resultado = (x+1) * num
        print(num,"x",x,"=",resultado)

#Prefeitura
def prefeitura():
    i=0
    vetor_salario=[]
    vetor_filho=[]
    for i in range(5):
        print("Pessoa",i+1)
        salario=float(input("Entre com sálario: "))
        filho=float(input("Entre com quantidade de filhos: "))
        vetor_salario.append(salario)
        vetor_filho.append(filho)
    soma_salario=sum(vetor_salario)
    soma_filho=sum(vetor_filho)
    media_salarios=soma_salario/5
    media_filhos=soma_filho/5
    print("O maior sálario é de:",max(vetor_salario))
    print("A média de sálario é de %.2f"%media_salarios)
    print("A média de filhos é de %.2f"%media_filhos)
    
#Sequencia Fibonacci----------------------------------------------------
def fibonacci():
    i=1
    sequencia = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    for i in range(20):
        ultimo = sequencia [-1]
        penultimo = sequencia [-2]
        sequencia.append(ultimo + penultimo)
    print(sequencia)

#20 Valores Inteiro------------------------------------------------
def inteiros():
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    maior = max(nums)
    menor = min(nums)
    soma = sum(nums)
    media = soma/20
    print("Maior numero:%.2f"%maior)
    print("Menor numero:%.2f"%menor)
    print("Soma dos numeros:%.2f"%soma)
    print("Media dos numeros:%.2f"%media)

#Vetores Inteiros---------------------------------------------------
def vetores(vetor):
    i=1
    vetor=[]
    novo_vetor=[]
    novo_vetor2=[]
    for i in range(10):
        num = int(input("Informe o valor do número: "))
        vetor.append(num)
    for num in range(len(vetor)):
        if num %2 == 0:
            novo_vetor.append(num*2)
        else:
            novo_vetor2.append(num*3)
    print(novo_vetor)
    print(novo_vetor2)
        
#juntar 2 vetores vetores--------------------------------------------------
def juntar_vetores():
    i=1
    lista1 = []
    lista2 = []
    for i in range(5):
        nums1=int(input("Digite número inteiro na lista 1: "))
        lista1.append(nums1)
        nums2=int(input("Digite números inteiros lista 2: "))
        lista2.append(nums2)
    lista1.extend(lista2)
    resultado=list(set(lista1))
    print("Lista 1 + Lista 2 =",resultado)

#vetores pares e impares
def vetor_par_impar():
    i=1
    vetor=[]
    vetor_par=[]
    vetor_impar=[]

    for i in range(15):
        num=int(input("Entre com número inteiro: "))
        vetor.append(num)
    for num in vetor:
        if num %2 == 0:
            vetor_par.append(num)
        else:
            vetor_impar.append(num)
    print("Todas as listas: ",vetor)
    print("Somente pares: ",vetor_par)
    print("Somente impar:",vetor_impar)

#calculadora------------------------------------------------------------------------
def somar(num1,num2):
    resultado = num1+num2 
    print(resultado)
def subtrair(num1,num2):
    resultado = num1-num2
    print(resultado)
def multiplicar(num1,num2):
    resultado = num1*num2
    print(resultado)
def dividir(num1,num2):
    resultado = num1/num2
    print(resultado)

#calcular a área de uma circunferencia-------------------------------------------
def circunferencia(r):
    area =3.14*(r*r)
    print(area)

#imc-----------------------------------------------------------------------------
def imc(peso,altura):
    imc = peso/(altura*altura)
    print(imc)
#calculo salario ----------------------------------------------------------------
def calcular_salario(hora,valor_hora,dias):
    salario = (hora*valor_hora)*dias
    print("Seu sálario é de %.2f"%salario)

#main----------------------------------------------------------------------------
def main():
    vetor=[]
    while True:
        print("="*60)
        print("ATIVIDADE 002 PROGRAMAÇÃO")
        print("="*60)
        print("Digite 1 para Calcular a Tabuada")
        print("Digite 2 para Prefeitura")
        print("Digite 3 para Sequencia Fibonacci")
        print("Digite 4 para 20 Valores Inteiros")
        print("Digite 5 para Vetores")
        print("Digite 6 para Juntar Vetores")
        print("Digite 7 para Vetor Impar e Par")
        print("Digite 8 para Calculadora")
        print("Digite 9 para Calcular a Área de um Circulo")
        print("Digite 10 para Calcular o IMC")
        print("Digite 11 para Calcular média do sálario")
        print("Digite 0 para Sair")
        opcao=input("Entre com a opção desejada: ")
        print("="*60)
        if opcao == '0':
            print("Saindo...")
            sleep(2)
            break
        elif opcao == '1':
            x=1
            num=int(input("Digite um numero: "))
            tabuada(num,x)
            sleep(2)
        elif opcao == '2':
            prefeitura()
            sleep(2)
        elif opcao == '3':
            fibonacci()
            sleep(2)
        elif opcao == '4':
            inteiros()
            sleep(2)
        elif opcao == '5':
            vetores(vetor)
            sleep(2)
        elif opcao == '6':
            juntar_vetores()
            sleep(2)
        elif opcao == '7':
            vetor_par_impar()
            sleep(2)
        elif opcao == '8':
            while True:
                print("CALCULADORA")
                print("Digite 1 para somar")
                print("Digite 2 para subtrair")
                print("Digite 3 para multiplicar")
                print("Digite 4 para dividir")
                print("Digite 0 para sair")
                escolha = input("Escolha uma opção: ")
                if escolha == '1':
                    num1=float(input("Entre com o 1° número: "))
                    num2=float(input("Entre com o 2° número: "))
                    somar(num1,num2)
                elif escolha == '2':
                    num1=float(input("Entre com o 1° número: "))
                    num2=float(input("Entre com o 2° número: "))
                    subtrair(num1,num2)
                elif escolha == '3':
                    num1=float(input("Entre com o 1° número: "))
                    num2=float(input("Entre com o 2° número: "))
                    multiplicar(num1,num2)
                elif escolha == '4':
                    num1=float(input("Entre com o 1° número: "))
                    num2=float(input("Entre com o 2° número: "))
                    dividir(num1,num2)
                elif escolha == '0':
                    print("Saindo...")
                    break
                else:
                    print("Opção invalida...")
                    print("Tente novamente")
                    sleep(2)
        elif opcao == '9':
            r=float(input("Entre com o raio da circunferência: "))
            circunferencia(r)
        elif opcao == '10':
            peso=float(input("Entre com o peso: "))
            altura=float(input("Entre com a altura: "))
            imc(peso,altura)
        elif opcao == '11':
            hora = float(input("Digite quantas horas trabalha por dia: "))
            valor_hora = float(input("Digite o quanto recebe por hora: "))
            dias = float(input("Digite quantos dias trabalha no mês: "))
            calcular_salario(hora,valor_hora,dias)
        else:
            print("Opção invalida...")
            print("Tente novamente")
            sleep(2)

if __name__ == "__main__":
    main()