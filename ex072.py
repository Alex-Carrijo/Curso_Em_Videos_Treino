contador = ('zero','UM', 'DOIS', 'TRES', 'QUATRO',
            'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE',
            'DOZE', 'TREZE', 'QUATORZE', 'QUINZE', 'DEZESSEIS',
            'DEZESSETE', 'DEZOITO','DEZENOVE', 'VINTE')
while True:
    x = int(input('Digite o numero de 0-20 para saber sua forma extensa: '))
    if x>-1 and x<21:
        break
    else:
        print('Valor não cadastrado na base de dados!')
print(contador[x])


