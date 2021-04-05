numero = int(input('\033[2;30;43mDigite um número: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
cores = {'azul': '\033[34m',
         'vermelho': '\033[31m',
         'limpa': '\033[m',
         'roxo': '\033[35m',
         'amarelo': '\033[33m'}
print('{}Unidade: {}'.format(cores['azul'], u))
print('{}Dezena: {}'.format(cores['amarelo'], d))
print('{}Centena: {}'.format(cores['roxo'], c))
print('{}Milhar: {}'.format(cores['vermelho'], m))
