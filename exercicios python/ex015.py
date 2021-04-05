km = float(input('Quantidade de Km rodados: '))
dias = float(input('Quantidade de dias: '))
q = km * 0.15
d = dias * 60
print('Você pagará R${:.2f} pelo aluguel do veículo.'.format(q + d))

