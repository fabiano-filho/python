l = float(input("Largura da parede: "))
a = float(input('Altura da parede: '))
A = l*a
print('A sua parede possui a dimensão {}x{} e tem como área {}m^2.\nPara pintar sua parede será necessário {}L de tinta'.format(l, a, A, A/2))
