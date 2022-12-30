termo = int(input('Digite o primeiro termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
fim = termo + razao*10
ordem = 1
print('Os termos da sua P.A é:')
for c in range(termo, fim, razao):
    print('{}° = {}'. format(ordem,c ))
    ordem += 1