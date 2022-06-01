print(50 * '=')
print('{:^50}'.format('BANCO CEV'))
print(50 * '=')


valor = int(input('Qual valor você quer sacar? R$'))
valor_total = valor
cedulas = 50
total_cedulas = 0

while True:
    if valor_total >= cedulas:
        valor_total -= cedulas
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f'Total de {total_cedulas} cédulas de R${cedulas}')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        total_cedulas = 0
        if valor_total == 0:
            break
print(50 * '=')
print('Volte sempre ao BANCO CEV! Tenha um bom dia!\n')
