from datetime import date

ano = date.today().year
totalidade = 0
maioridadehomem = 0
nomevelho = 0
meninas = 0

for c in range(1, 5):
    print('______{}°______'.format(c) )
    nome = str(input('Digite nome: ')).strip()
    sexo = str(input('Digite o sexo [M/F]: ')).strip()
    nascimento = int(input('Digite o ano de nascimento: '))

    idade = ano - nascimento
    totalidade += idade

    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if sexo in 'Ff' and idade < 20:
        meninas += 1


mediaidade = totalidade/4
print('A media de idade do grupo é: {}'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('A quantidade de mulheres menores de 20 anos é {}'.format(meninas))