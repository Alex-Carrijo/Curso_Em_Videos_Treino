'''valor = int(input('Valor do saque: '))
notas50 = notas = notas20 = notas10 = notas1 = resto50 = resto20 = resto10 = 0
while True:
    if valor > 50:
        resto50 = valor % 50
        notas50 = valor // 50
    if resto50 > 20:
        resto20 = resto50 % 20
        notas20 = resto50 // 20
    if resto20 > 10:
        resto10 = resto20 % 10
        notas10 = resto20 // 10
    if resto20 < 10:
        resto10 = resto20 % 10
    break
print(f'Serão {notas50} notas de 50')
print(f'Serão {notas20} notas de 20')
print(f'Serão {notas10} notas de 10')
print(f'Serão {resto10} notas de 1')'''
print('='*20)
print('{:^30}'.format('BANCO CEV'))
print('='*20)
valor = int(input('Que valor você sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break