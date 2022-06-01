media = cont_mulheres = maior_idade_M = 0
pessoa_maior_idade = ''
for pessoa in range(1, 5):
    print(5 * '-', f'{pessoa}ª PESSOA', 5 * '-')
    nome = input('Nome: ').capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper()

    media += idade
    if sexo == 'F':
        if idade < 20:
            cont_mulheres += 1
    if sexo == 'M':
        if idade > maior_idade_M:
            maior_idade_M = idade
            pessoa_maior_idade = f'{nome}'

print(f'A média de idade do grupo é de {media/pessoa:.1f} anos')
print(
    f'O homem mais velho tem {maior_idade_M} anos e se chama {pessoa_maior_idade}')
print(f'Ao todo são {cont_mulheres} mulheres com menos de 20 anos')
