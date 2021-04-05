n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
n3 = int(input('Terceiro valor: '))
cores = {'azul':'\033[34m',
         'vermelho':'\033[31m',
         'limpa':'\033[m',
         'roxo':'\033[35m',
         'amarelo':'\033[33m'}
if n1 > n2 > n3 or n1 > n3 > n2:
    print('O {}maior{} valor é {}'.format(cores['azul'], cores['limpa'], n1))
if n2 > n1 > n3 or n2 > n3 > n1:
    print('O {}maior{} valor é {}'.format(cores['azul'], cores['limpa'], n2))
if n3 > n2 > n1 or n3 > n1 > n2:
    print('O {}maior{} valor é {}'.format(cores['azul'], cores['limpa'], n3))
if n1 < n2 < n3 or n1 < n3 < n2:
    print('{} é o {}menor{} valor'.format(n1, cores['vermelho'], cores['limpa']))
if n2 < n1 < n3 or n2 < n3 < n1:
    print('{} é o {}menor{} valor'.format(n2, cores['vermelho'], cores['limpa']))
if n3 < n2 < n1 or n3 < n1 < n2:
    print('{} é o {}menor{} valor'.format(n3, cores['vermelho'], cores['limpa']))

