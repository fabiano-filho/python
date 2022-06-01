while True:
    print(50 * '-')
    print('{:^50}'.format('TABUADA'))
    print(50 * '-')
    num = int(input('Quer ver a tabuada de qual valor? [0 para parar] '))
    if num <= 0:
        break
    else:
        for i in range(1, 11):
            print(f'{num} X {i:2} = {num * i}')
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')
