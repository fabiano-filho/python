print('Gerador de PA')
print(22*'=-')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
cont = 1
while cont <= 10:
    print(f'{primeiro_termo}', end=" -> ")

    primeiro_termo += razao
    cont += 1
print('FIM')
