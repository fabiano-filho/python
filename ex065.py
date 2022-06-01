
soma = maior = i = menor = 0
escolha = 'S'
while escolha in 'S':
    numero = int(input('Digite um número: '))
    soma += numero
    i += 1

    if i == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero
    escolha = input('Quer continuar? [S/N] ').upper().strip()[0]


media = soma / i
print(soma)
print(f'Você digitou {i} números e a média foi {media}')
print(f'{maior} E {menor}')
