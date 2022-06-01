from datetime import date
menor_idade = 0
maior_idade = 0
for pessoa in range(1, 8):
    ano = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
    if date.today().year - ano > 18:
        maior_idade += 1
    else:
        menor_idade += 1
print(
    f'Ao todo tivemos {maior_idade} pessoas maiores de idade\nE também tivemos {menor_idade} menores de idade')
