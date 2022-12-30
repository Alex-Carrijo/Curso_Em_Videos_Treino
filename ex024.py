cidade = str(input('Digite o nome da cidade que voce nasceu: '))
name = cidade.lower()
nome = name.split()
print("A sua cidade comeca com Santo: {}".format('santo' in nome[0]))

# metodo dele:
# cid = str(input('Em que cidade voce nasceu?')).strip()
# print(cid[:5].upper() == 'SANTO')