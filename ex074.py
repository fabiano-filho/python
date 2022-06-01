from random import randint

num_sorteados = (randint(0, 9), randint(
    0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

# num_organizado = sorted(num_sorteados)

print("Os valores sorteados foram: ", end="")
for n in range(0, 5):
    print(num_sorteados[n], end=" ")

# print(f'\nO maior valor foi {num_organizado[-1]}')
# print(f'O menor valor foi {num_organizado[0]}')

print(f'O maior valor foi {max(num_sorteados)}')
print(f'O maior valor foi {min(num_sorteados)}')
