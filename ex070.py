total = maior_que_1000 = mais_barato = cont = 0
prod_barato = ''

print(50 * '-')
print('{:^50}'.format('LOJA SUPER BARATÃO'))
print(50 * '-')

while True:
    nome_prod = input('Nome do Produto: ').title()
    preco_prod = float(input('Preço: R$'))
    cont += 1
    continuar = ''
    total += preco_prod
    if cont == 1:
        mais_barato = preco_prod
        prod_barato = nome_prod
    if preco_prod < mais_barato:
        mais_barato = preco_prod
        prod_barato = nome_prod
    if preco_prod > 1000:
        maior_que_1000 += 1

    while continuar not in 'SN':
        continuar = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if continuar in 'N':
        break

print()
print('{:-^50}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {maior_que_1000} produtos custando mais de R$1000.00')
print(
    f"O produto mais barato foi {prod_barato} que custa R${mais_barato:.2f}\n")
