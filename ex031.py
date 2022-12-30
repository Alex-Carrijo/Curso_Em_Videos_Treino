x = float(input('Quantos quilometros tem a viagem:'))
if x > 200:
    print('O valor da passagem é: R${:.2f} '.format(x*0.45))
else:
    print('O valor da passagem é: R${:.2f} '.format(x*0.50))