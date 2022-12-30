x = float(input('Digite o salario do funcionario: R$'))
'''if x > 1250:
    print('Seu novo salario é: R${:.1f}'.format(x*1.1))
else:
    print('Seu novo salario é: R${:.1f}'.format(x*1.15))'''
if x > 1250:
     x = x*1.1
else:
     x = x*1.15
print('O novo salario é: R${:.2f}'.format(x))
