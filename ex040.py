x1 = float(input('Digite a primeira nota: '))
x2 = float(input('Digite a segunda nota: '))
media = (x1 + x2) / 2
if media > 7:
    print('PARABÉNS! você passou de ano! :D , sua media foi {:.1f} '.format(media))
elif media > 4.9 and media < 7:
    print('Você está de recuperação, melhore :( , sua media foi {:.1f} !'.format(media))
else:
    print('Você reprovou! tente outra vez ;) , sua media foi {:.1f} '.format(media))