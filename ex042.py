print('-='*15)
print('Analisador de Triangulos')
print('-='*15)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Forma ', end='' )
    if r1 == r2 == r3:
        print('o triângulo equilátero!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('o triângulo isóceles!')
    else:
        print('o triângulo  escaleno!')
else:
    print('Não forma triangulo!')