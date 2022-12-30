peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura em metros:'))
imc = peso / (altura**2)
if imc < 18.5:
    print('Você está abaixo do peso seu IMC é {:.2f}!'.format(imc))
elif imc < 25.1:
    print('Você está com o peso ideal seu IMC é {:.2f}!'.format(imc))
elif imc < 30.1:
    print('Você está com sobrepeso seu IMC é {:.2f}!'.format(imc))
elif imc < 40.1:
    print('Você está com obesidade seu IMC é {}!'.format(imc))
else:
    print('você está com obesidade morbida seu IMC é {}!'.format(imc))