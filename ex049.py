print(12*'-', f'  TABUADA  ', 12*'-')
numero = int(input('Digite um número: '))
for i in range(1, 11):
    print(f'{numero} X {i:2} = {i * numero}')
