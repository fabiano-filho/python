num = int(input('Digite um número: '))
cont = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(f'\033[32m{i}', end=" ")
        cont += 1
    else:
        print(f'\033[31m{i}', end=" ")
print(f'\n\033[mO número {num} foi divisivel {cont} vezes')
if cont == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele é PAR!')
