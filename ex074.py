from random import randint
#numeros = random.sample(range(0,100),5)
nu = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ',end='')
for n in nu:
    print(f'{n} ',end='')

print(f'\nO maior valor foi: {max(nu)}')
print(f'O menor valor foi: {min(nu)}')
