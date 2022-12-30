print('Você está comprando um produto no valor de R$100, o valor poderá ser alterado dependendo da forma de pagamento')
print('''Formas de pagamento: 
[1] À vista dinheiro/Cheque
[2] À vista no cartão
[3] Para 2x no cartão
[4] Para mais de 3X no cartão ''')
pagamento = int(input('Digite qual a forma de pagamento: '))
x = 100
if pagamento == 1:
    print('Você está pagando com cheque/dinheiro, o valor total é R${}'.format(x*0.9))
elif pagamento == 2:
    print('Você está pagando em 1X no cartão, o valor total é R${}'.format(x*0.95))
elif pagamento == 3:
    print('Você está pagando em 2X no cartão, o valor total é R${}'.format(x))
elif pagamento == 4:
    print('Você está pagando em muitas parcelas, o valor total é R${}'.format(x*1.2))
else:
    print('Opçao invalida de pagamento. Tente novamento!')