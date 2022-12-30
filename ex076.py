lista = ('maçã', 5.49, 'pera', 7.49, 'lapis', 1.49, 'caderno', 9.99,'Livro', 39.99,
         'Borracha', 1.99, 'Caneta', 1.99,'Celular', 1999.99)
len(lista)
print('__'*20)
print('LISTA')
print('__'*20)
i=0
while i < len(lista):
    print(f'{lista[i]:.<30} R${lista[i+1]:>8.2f}')
    i += 2
print('__'*20)
'''for i in range(0, len(lista), 2)
        print(f'{lista[i]:.<30}{lista[i+1]:>8.2f}')
 '''
