tabela_times = ('Atlético-MG', 'Palmeiras',	'Flamengo',	'Fortaleza', 'Bragantino',
                'Corinthians', 'Internacional', 'Fluminense', 'Cuiabá', 'Athletico-PR',
                'Atlético-GO', 'São Paulo',	'Ceará', 'Santos', 'Bahia',
                'Juventude', 'Grêmio', 'América-MG', 'Sport', 'Chapecoense',
                )
print()
print(140*'-')
print('Os 5 primeiros times são: ', end="")
for i in range(0, 5):
    if i < 4:
        print(f'{tabela_times[i]}', end=", ")
    if i == 4:
        print(f'{tabela_times[i]}.')

print(140*'-')
print('Os quatro ultimos times são: ', end="")
for i in range(1, 5):
    if i < 4:
        print(f'{tabela_times[-i]}', end=", ")
    if i == 4:
        print(f'{tabela_times[-i]}.')
print(140*'-')
print('Em ordem alfabetica: ', sorted(tabela_times))
print(140*'-')
if 'Chapecoense' in tabela_times:
    print(
        f"O time Chapecoense está na posição {tabela_times.index('Chapecoense')+ 1}")
print(140*'-')
print()
