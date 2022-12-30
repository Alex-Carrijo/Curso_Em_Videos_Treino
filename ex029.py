x = float(input('Velocidade do carro:'))
if x > 80:
   m = (x - 80) * 7
   print('Voce ultrapassou o limite de 80km/h  e recebeu uma muta de: {:.2f}'.format(m))
else:
   print('Voce nao ultrapassou o limite de velocidade!!')