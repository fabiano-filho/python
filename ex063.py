cont = t1 = 0
t2 = 1
print(50 * '-')
print('Sequência de Fibonacci')
print(50 * '-')
termos = int(input('Quantos termos você quer mostrar? '))
print(50 * '-')
while cont < termos:
    fibonacci = t1
    t3 = t1 + t2
    print(fibonacci, end=" -> ")
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')
