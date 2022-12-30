nome = str(input("Digite o seu nome completo: ")).strip()
name = nome.split()
print('Seu primeiro nome é: {}'.format(name[0]))
print('Seu ultimo nome é: {}'.format(name[len(name)-1]))