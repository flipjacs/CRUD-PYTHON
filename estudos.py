n1=int(input("Digite um número: "))
n2=int(input("Digite um número: "))
opcao = 0
while opcao != 5:
    print('=-='*10)
    print('''[1] Somar
[2] Multiplicar 
[3] Maior
[4] Novos números
[5] Sair''')
    opcao = int(input("Qual é sua escolha? "))
    if opcao == 1:
        soma=n1+n2
        print(f"A soma de {n1} e {n2} é {soma}")
        opcao=5
    elif opcao==2:
        produto=n1*n2
        print(f'A multiplicação de {n1} e {n2} é {produto}')
        opcao=5
    elif opcao==3:
        if n1>n2:
            print(f'O número {n1} é maior que {n2}')
            opcao=5
        elif n2>n1:
            print(f'O número {n2} é maior que {n1}')
            opcao=5
        else:
            print("Os dois números são iguais!")
            opcao=5
    elif opcao==4:
        n1=int(input("Digite um número: "))
        n2=int(input("Digite um número: "))
    else:
        print("Insira uma opção válida")
    print('=-='*10)
print("Fim do programa")