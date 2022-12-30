casa = float(input('Qual é o valor da casa? '))
salario = float(input('Qual e o valor do seu salário? '))
anos = int(input('Em quantos anos você quer pagar a casa? '))
valor = casa / (anos * 12)
porcentagem = salario * 0.3
if valor >= porcentagem:
    print('O financiamento foi negado seu salário não é compativel com o valor do financiamento!!')
else:
    print('Você foi aprovado a comprar a casa de R${}, com financiamento com {} anos de duração pelo valor da parcela de {:.1f}!!'.format(casa, anos, valor))
