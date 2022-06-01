print(26*'=')
print('   10 TERMOS DE UMA PA   ')
print(26*'=')
primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for i in range(primeiro_termo, 10 * razao, razao):
    print(i, end=" -> ")
print('FIM')
