def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except( ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um numero inteiro valido.\033[m")
            continue
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO: por favor, digite um numero real válido.\033[m")
            continue
        except (KeyboardInterrupt):
            print("\n\033[31mUsuario preferiu não digitar esse numero.\033[m")
            return 0
        else:
            return n
num = leiaInt("Digite um valor Inteiro: ")
n2 = leiaFloat('Digite um valor real: ')
print(f"O valor inteiro foi {num} e o real foi {n2}")