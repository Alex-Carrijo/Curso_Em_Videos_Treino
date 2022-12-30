lista = []
todas = []
cont = 0
while True:
    nome = lista.append(str(input('Nome: ')))
    nota1 = lista.append(float(input('Nota 1: ')))
    nota2 = lista.append(float(input('Nota 2: ')))
    if len(lista) == 3:
        todas.append(lista[:])
        lista.clear()
    r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    while r not in 'SN':
        r = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    if r == 'N':
        break
print(f'{"NO.":<4}{"NOME":<10}{"MEDIA":>8}')
for c in todas:
    media = (c[1] + c[2]) / 2
    cont += 1
    print(f'{cont:<4}{c[0]:<10}{media:>8.1f}')

'''
#Aula 89
ficha = ()

while True:
    nome = str(input('Nome:'))
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media]
    r = str(input('Deseja continuar[S/N]: ').upper().strip()[0]
    while r not in 'SN':
        r = str(input('Deseja continuar[S/N]: ').upper().strip()[0]
    if r == 'N':
        break
print('=-'*26)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('=-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrae notas de qual aluno? (999 interrompe): ))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<VOLTE SEMPRE>>>')

'''