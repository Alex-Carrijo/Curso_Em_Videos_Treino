from datetime import date
x = date.today().year
dados = {}
dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimeto: '))
dados['idade'] = x - ano
dados['ctps'] = str(input('Numero da carteira de trabalho (0) para não possui: '))
if dados['ctps'] not in '0':
    dados['ano'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Salário: '))
    dados['aposentadoria'] = (dados['ano'] - ano + 35)
print('=-'*12)
for k, v in dados.items():
    print(f'{k}:  {v}')
print('=-'*12)
