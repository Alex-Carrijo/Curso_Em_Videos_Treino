x = int(input('Digite um numero:'))
y = int(input('Digite outro numero:'))
z = int(input('Digite outro numero:'))
# verificando o maior numero
maior = z
if x > y and x > z:
   maior = x
if y > x and  y > z:
        maior = y
print('O maior numero é {}'.format(maior))
# verificando o menor numero
menor = z
if x < y and x < z:
        menor = x
if y < x and y < z:
        menor = y
print('O menor numero é {}'.format(menor))
