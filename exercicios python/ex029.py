from time import sleep
velo = int(input('Qual a velocidade do carro? '))
m = (velo - 80) * 7
print('PROCESSANDO...')
sleep(2)
if velo > 80:
    print('MULTADO! Você ultrapassou o limite de velocidade permitido, deverá pagar R${:.2f} de multa.'.format(m))

print('Tenha um bom dia! Dirija com segurança!')
