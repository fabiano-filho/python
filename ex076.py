produtos = (
    'Lapis', 2.30,
    'Caneta', 5.00,
    'Caderno', 25.00,
    'Estojo', 3.00
)
print(50*'-')
print('{:^50}'.format('LISTAGEM DE PREÇO'))
print(50*'-')
x = 0
cont = 1
for i in range(4):
    print(f'{produtos[x]:.<40}R$ {produtos[cont]:7.2f}')
    x += 2
    cont += 2
print(50*'-')

# OUTRA FORMA DE FAZER:
# for i in range(len(produtos)):
#     if i % 2 == 0:
#         print(f'{produtos[i]:.<30}', end='')
#     else:
#         print(f'R${produtos[i]:7.2f}')
