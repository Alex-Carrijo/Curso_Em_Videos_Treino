pessoas = {'nome':'Alex', 'sexo': 'M', 'idade': '21'}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()
for k in pessoas.keys():
    print(k)
print()
for v in pessoas.values():
    print(v)
print()
for k, v in pessoas.items():
    print(k)
    print(v)
print()
del pessoas['sexo']
pessoas['nome'] = 'Lucas'
pessoas['peso'] = 60
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()
print()
brasil = []
estado1 = {'uf': 'Sao Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
brasil.clear()

print()
print()
estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = str(input('Digite o estado: '))
    estado['sigla'] = str(input('Digite a sigla: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    for k, v in e.items():
        print(f'O campo{k} tem valor {v}')