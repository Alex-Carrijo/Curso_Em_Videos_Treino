termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
fim = termo + razao*10
ordem = 1
total = 0
quantidade = int(input('Você quer ver quantos termos ? '))
while quantidade !=0:
    total += quantidade
    while ordem <= total:
        print('{} -> '. format(termo), end='')
        termo += razao
        ordem += 1
    print('PAUSA')
    quantidade = int(input('Você quer ver mais alguns termos, quantos ? '))
print("Foram mostratos {} termos da PA".format(total))