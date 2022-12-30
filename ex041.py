from datetime import date
ano =  int(input('Digite o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual - ano
print('A idade do atleta é {} anos, sua categoria é:'.format(idade))
if idade < 10:
    print('Classificação MIRIN!')
elif idade < 15:
    print('Classificação INFANTIL!')
elif idade < 20:
    print('Classificação JUNIOR!')
elif idade < 21:
    print('Classificação SENIOR!')
else:
    print('Classificação MASTER')
