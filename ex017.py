from math import sqrt
catetoO = float(input('Qual o comprimento do cateto oposto? '))
catetoa = float(input('Qual o comprimento do cateto adjacente? '))
hipotenusa = sqrt(catetoO ** 2 + catetoa ** 2)
print('O valor da hipotenusa é {:.2f}'.format(hipotenusa))
