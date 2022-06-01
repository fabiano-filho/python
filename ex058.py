from random import randint


print('Sou seu computador...')
print('Acabei de pensar um um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
tentativas = 0
numero_aleatorio = randint(0, 10)
while True:
    resposta = int(input('Qual é seu palpite? '))
    tentativas += 1
    if resposta == numero_aleatorio:
        tentativas += 1
        print(f'Parabéns! Você acertou com {tentativas} tentativas.')
        break
    else:
        if resposta < numero_aleatorio:
            print('Mais... Tente mais uma vez.')

        elif resposta > numero_aleatorio:
            print('Menos... Tente mais uma vez.')
