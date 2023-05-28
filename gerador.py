import random
import string


def gerar_senha(comprimento, caracteres):
    senha = ''
    for _ in range(comprimento):
        senha += random.choice(caracteres)
    return senha


def main():
    comprimento = int(input("Digite o comprimento da senha desejada: "))
    caracteres = string.ascii_letters + string.digits

    senha = gerar_senha(comprimento, caracteres)
    print("A senha gerada é:", senha)


if __name__ == '__main__':
    main()
