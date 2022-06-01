nome = str(input('Digite uma frase: ')).upper().strip()
cores = {'azul':'\033[34m',
         'vermelho':'\033[31m',
         'limpa':'\033[m',
         'roxo':'\033[35m',
         'amarelo':'\033[33m'}
print('A letra {}A{} aparece {}{} vezes\033[m'.format(cores['roxo'],cores['limpa'], cores['azul'], nome.count('A')))
print('A letra {}A{} aparece a primeira vez na {}posição {}\033[m'.format(cores['roxo'],cores['limpa'], cores['azul'], nome.find('A') + 1))
print('A letra {}A{} aparece a última vez na {}posição {}'.format(cores['roxo'],cores['limpa'], cores['azul'], nome.rfind('A') + 1))
