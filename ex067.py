while True:
    print('~~'*20)
    print('Tabuada')
    print('~~'*20)
    n = int(input('Digite um numero para obter sua tabuada: '))
    if n < 0:
        print('Tabuada encerrada!')
        break
    for t in range(1,11):
        print(f'{n}X{t} = {n*t}')
