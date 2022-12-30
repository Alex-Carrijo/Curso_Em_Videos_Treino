lista = []
while True:
     x = (int(input('Digite o valor que deseja adicionar: ')))
     if x not in lista:
        lista.append(x)
        print('Valor adicionado com sucesso...')
     else:
         print('Valor duplicado não irei adicionar')
     lista.sort()
     r = str(input('Deseja encerrar [S/N]: ')).upper().strip()[0]
     while r not in 'SN':
         r = str(input('Deseja encerrar [S/N]: ')).upper().strip()[0]
     if r == 'N':
         break
print(lista)