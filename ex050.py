soma = 0
c = 0
for i in range(1, 7):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma += numero
        c += 1
print(f'Dos 6 números digitados {c} são pares e a soma deles é {soma}')
