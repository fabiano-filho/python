numero = int(input('\033[34mDigite um número: '))
resultado = numero % 2
if resultado == 0:
    print('\033[35mO número {} é PAR'.format(numero))
else:
    print('\033[31mO número {} é ÍMPAR'.format(numero))
