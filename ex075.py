nu = (int(input('Digite um numero: ')),int(input('Digite outro numero: ')),
      int(input('Digite outro numero: ')),int(input('Digite mais um numero: ')))

print(f'Você digitou os valores: {nu}')
print(f'O numero 9 apareceu {nu.count(9)} vezes')
if 3 in nu:
      print(f'O numero 3 aparece na posição {nu.index(3)+1}°')
else:
      print('Não foi digitado o numero 3')
print('Os valores pares são: ', end='')
for n in nu:
      if n % 2 == 0:
            print(f'{n} ', end='')


