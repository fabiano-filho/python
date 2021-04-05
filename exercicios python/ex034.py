valor = float(input('\033[35mQual o salário do funcionário? '))
if valor <= 1250:
    salario = (valor * 0.15)
    salario_ajustado = salario + valor
    print('\033[34mA partir do ajuste salarial o funcionário passa a receber \033[32mR${:.2f}\033[34m reais'.format(salario_ajustado))
else:
    salario = valor * 0.10
    salario_ajustado = salario + valor
    print('\033[34mA partir do ajuste salarial o funcionário passa a receber \033[32mR${:.2f}\033[34m reais'.format(salario_ajustado))
