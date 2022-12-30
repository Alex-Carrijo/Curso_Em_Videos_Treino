print('-='*15)
print('Analisador de Triangulos')
print('-='*15)
r1= float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos podem formar um triangulo')
else:
    print('Nao e possivel formar um triangulo com esses segmentos')