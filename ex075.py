v1 = int(input('Digite um número: '))
v2 = int(input('Digite outro número: '))
v3 = int(input('Digite mais um número: '))
v4 = int(input('Digite o ultimo numero: '))
valores = (v1, v2, v3, v4)
print(f"Você digitou os valores {valores}")
print(f'O valor 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

for valor in valores:
    if valor % 2 == 0:
        par = valor

print(f"Os valores pares digitados foram {par}")
