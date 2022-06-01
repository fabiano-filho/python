import os

cont_maior_18 = cont_homem_cadastrado = cont_mulher_menor_20 = 0
while True:
    print(50 * '-')
    print('{:^50}'.format('CADASTRE UMA PESSOA'))
    print(50 * '-')

    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()[0]

    continuar = input('Deseja continuar? [S/N] ').upper().strip()[0]

    if sexo == 'F' and idade < 20:
        cont_mulher_menor_20 += 1

    if idade >= 18:
        cont_maior_18 += 1

    if sexo == 'M':
        cont_homem_cadastrado += 1

    if continuar == 'N':
        print()

        break

print(f'''
Total de pessoas com mais de 18 anos: {cont_maior_18}
Ao todo temos {cont_homem_cadastrado} homens cadastrados
E temos {cont_mulher_menor_20} mulheres com menos de 20 anos
''')
os.system('pause')
os.system('cls')
