frase = str(input('Digite uma frase: ')).lower().strip()
print("A frase tem {} de a.".format(frase.count('a')))
print('A primeira letra A esta na posicao: {}.'.format(frase.find('a')+1))
print('A ultima letra A esta na posicao: {}.'.format(frase.rfind('a')+1))