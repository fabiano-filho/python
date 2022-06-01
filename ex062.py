print('Gerador de PA')
print(22*'=-')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
cont = 0
termos = 10
while termos != 0:
    for i in range(0, termos):
        print(f'{primeiro_termo}', end=" -> ")
        primeiro_termo += razao
        cont += 1
    print('PAUSA')
    termos = int(input('\nQuantos termos você quer mostrar a mais? '))

print(f'Progressão finalizada com {cont} termos mostrados.')
