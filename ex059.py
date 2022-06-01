n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

while True:

    print(7*'-', '[ 1 ] Somar')
    print(7*'-', '[ 2 ] Multiplicar')
    print(7*'-', '[ 3 ] Maior')
    print(7*'-', '[ 4 ] Inserir novos números')
    print(7*'-', '[ 5 ] Sair do programa')
    escolha = int(input('>>>> Qual é a sua escolha? '))
    print()
    if escolha == 5:
        break
    elif escolha == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
        print(30*'-=')
    elif escolha == 2:
        multiplicar = n1 * n2
        print(f'{n1} * {n2} = {multiplicar}')
        print(30*'-=')
    elif escolha == 3:
        if n1 > n2:
            maior = n1
            print(f'Entre os número {n1} e {n2}, o maior é {maior}')
            print(30*'-=')
        else:
            maior = n2
            print(f'Entre os número {n1} e {n2}, o maior é {maior}')
            print(30*'-=')
    elif escolha == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    else:
        print('Opção inválida! Tente novamente.')
