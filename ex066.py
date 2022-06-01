cont = soma = 0
while True:
    numero = int(input('Digite um número [999 para parar]: '))
    if numero == 999:
        break
    cont += 1
    soma += numero
if cont > 0:
    print(f'Você digitou {cont} números e a soma deles foi {soma}')
print('Volte sempre!')
