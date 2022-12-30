from datetime import date
sexo = input('Qual e o seu sexo feminino ou masculino: ')
if sexo == 'masculino':
    ano = float(input('Digite o ano que você nasceu: '))
    atual = date.today().year
    idade = atual - ano
    h = 18 - idade
    print('Quem nasceu em {} tem {} em {}'.format(ano, idade, atual))
    if idade < 18:
        print('Você ainda não precisa se alistar ainda falta {} anos!'.format(h))
        print('Voce deveria ter se alistado à {} anos '.format(h))
        print('Seu alistamento será em {}'.format(atual - h * -1))
    elif idade == 18:
        print('Está na hora de se alistar para o exercito!')

    else:
        print('Já se passou da idade de alistamento!')
        print('Voce deveria ter se alistado à {} anos '.format(h * -1))
        print('Seu alistamento foi em {}'.format(atual - h * -1))
else:
    print('Não faz isso garota!')