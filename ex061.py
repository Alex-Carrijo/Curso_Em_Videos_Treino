termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
fim = termo + razao*10
ordem = 1
print('Os termos da sua P.A é:')
'''while ordem != 11:
    print('{}° = {}'. format(ordem,termo+razao*(ordem-1) ))
    ordem += 1'''

while ordem <= 10:
    print('{} -> '.format(termo), end=' ')
    termo += razao
    ordem +=1
print('FIM')