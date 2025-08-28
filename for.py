contador = 0
for contador in range(5):
    print("Paciente %i"%contador)
    altura = float(input("Entre com a altura: "))
    sexo = str.upper(input("Entre com o sexo(M ou F): "))
    if(sexo == 'M'):
        peso = (72.7*altura)-58
        print("Seu peso ideal é %.2f"%peso)
    elif(sexo == 'F'):
        peso = (62.1*altura)-44.7
        print("Seu peso ideal é %.2f"%peso)
    else:
        print("Entre com uma opção válida para sexo (M ou F)")
   
    