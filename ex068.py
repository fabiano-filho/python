from random import randint

cont = 0

print(50 * '=')
print('{:^50}'.format('PAR OU ÍMPAR'))
print(50 * '=')

while True:

    pc = randint(1, 10)
    num = int(input('Digite um valor: '))
    escolha = input('Par ou Ímpar? [P/I] ').upper().strip()[0]
    resultado = num + pc

    if escolha not in 'PI':
        print('Caractere inválido. Tente novamente')

    else:
        print(50 * '-')
        print(f'Você jogou {num} e o computador {pc}. Total de {pc + num}')
        print(50 * '-')
        if escolha == 'P':
            if resultado % 2 == 0:
                print('Deu PAR, você VENCEU!')
                print('Vamos jogar novamente...')
                cont += 1
            else:
                print('Deu ÍMPAR, você PERDEU!')
                print(50 * '-')
                print(f'GAME OVER! Você venceu {cont} vezes.')
                playAgain = input(
                    'Deseja jogar novamente? [S/N] ').upper().strip()[0]
                if playAgain == 'S':
                    cont = 0

                else:
                    break
        if escolha == 'I':
            if resultado % 2 == 0:
                print('Deu PAR, você PERDEU!')
                print(50 * '-')
                print(f'GAME OVER! Você venceu {cont} vezes.')
                playAgain = input(
                    'Deseja jogar novamente? [S/N] ').upper().strip()[0]
                if playAgain == 'S':
                    cont = 0

                else:
                    break
            else:
                print('Deu ÍMPAR, você VENCEU!')
                print('Vamos jogar novamente...')
                cont += 1
