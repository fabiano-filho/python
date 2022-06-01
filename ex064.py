

soma = i = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break

    else:
        soma += num
print(f'Você digitou {i} números e a soma deles foi {soma}.')
