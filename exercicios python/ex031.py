distancia = float(input('Qual a distância de seu destino? '))
print('Você esta prestes a realizar uma viagem de {} km'.format(distancia))
if distancia <= 200:
    print('O valor da viagem é de R${:.2f}'.format(distancia * 0.5))
else:
    print('O valor da viagem é de R${:.2f}'.format(distancia*0.45))
