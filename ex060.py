numero = int(input('Digite um número para calcular seu Fatorial: '))
fatorial = 1
contador = numero
print(f'Calculando {numero}! = ', end="")
while contador > 0:
    print(f'{contador}', end="")
    print(' x ' if contador > 1 else ' = ', end="")
    fatorial *= contador
    contador -= 1
print(f'{fatorial}')
