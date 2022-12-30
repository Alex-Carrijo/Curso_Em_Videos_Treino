sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dado invalido. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
print('Você digitous {}, obrigado pela colaboração! '.format(sexo))