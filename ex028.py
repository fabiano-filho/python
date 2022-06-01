from random import randint
from time import sleep
x = randint(1, 10)
print('-=-' * 18)
print('Tente adivinhar! Vou pensar em um número de 1 a 10')
print('-=-' * 18)
numero = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if numero == x:
    print('Parabéns, você acertou!')
else:
    print('O número correto era {}'.format(x))
    print('####' * 3,'VOCÊ PERDEU, EU GANHEI!!!!', '####' * 3)
print('-*-' * 8, 'FIM', '-*-' * 8)
