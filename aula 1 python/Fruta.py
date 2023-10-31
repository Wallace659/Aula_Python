# faça um programa que pede para o usuário escrever o nome de uma fruta
# e que fique em um loop infinito até o usuário escrever "fim" no lugar do nome da fruta.

while True:
    fruta = str(input("Digite o nome de uma fruta:"))

    if fruta.lower() == "fim":
        break