print('\033[35mX' * 26)
print('\033[7;mANALISADOR DE TRIÂNGULOS\033[0;35m X\033[m')
print('\033[35mX' * 26)
a = float(input('\033[34mPrimeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if b - c < a < b + c and a - c < b < a + c and a - b < c < a + b:
    print('\033[32mOs seguimentos acima podem \033[32mFORMAR\033[32m um TRIÂNGULO')
else:
    print('\033[31mOs seguimentos acima \033[31mNÃO \033[m\033[31mpodem FORMAR um TRIÂNGULO')
