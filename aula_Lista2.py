test = list()
test.append('Alex')
test.append(21)
galera = list()
galera.append(test[:])
test[0] = 'Maria'
test[1] = 22
galera.append(test[:])
print(galera)

todos = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(todos)
print(todos[0][0])
for p in todos:
    print(f'{p[0]}, tem {p[1]} anos de idade!')

pessoal = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoal.append(dado[:])
    dado.clear()
print(pessoal)
totmaior = totmenor = 0
for p in pessoal:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade!')
        totmenor += 1
print(f'Temos {totmaior} maiores e {totmenor} menor de idade!')