listaDeValores = [input(f'Digite um valor na posição {i}: ') for i in range(4)]
print(f'Você digitou os valores: {listaDeValores}')
print(
    f'O maior valor digitado foi: {max(listaDeValores)} nas posições:', end=' ')
for i, v in enumerate(listaDeValores):
    if max(listaDeValores) == v:
        print(f'{i}...', end=' ')
print()
print(
    f'O menor valor digitado foi: {min(listaDeValores)} nas posições:', end=' ')
for i, v in enumerate(listaDeValores):
    if min(listaDeValores) == v:
        print(f'{i}...', end=' ')
