from time import sleep
n = str(input('\033[31mDigite seu nome completo: ')).strip().capitalize()
print('\033[2;30;45mAnalisando seu nome...\033[m')
sleep(2)
print('\033[34mSeu nome em letras maiúsculas é\033[35m',n.upper())
print('\033[34mSeu nome em letras minúsculas é\033[35m',n.lower())
dividido = n.split()
junto = ''.join(dividido)
print('\033[34mSeu nome tem \033[35m{} letras'.format(len(junto)))

print('\033[34mSeu primeiro nome é {} e possui \033[35m{} letras'.format(dividido[0], len(dividido[0])))





