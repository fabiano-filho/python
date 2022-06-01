cont = 0
c = 0
for i in range(1, 501):
    if i % 2 != 0:
        if i % 3 == 0:
            cont += i
            c += 1
print(
    f'No intervalo de 1 a 500, {c} são numeros ímpares e divisiveis por 3. A soma de todos esses valores é de {cont}')
