frutas = ["UVA", "PÊRA", "MELÃO", "MAÇA", "BANANA", "ACEROLA", "ABACAXI"]

while True:
    print(frutas)
    menu = int(input("""
        Escolha uma opção:
        1 - Excluir a última fruta
        2 - Escolher qual fruta excluir
        0 - Sair
"""))
    match menu:
        case 1:
            frutas.pop()
        case 2:
            print(frutas)
            posicao = int(input("Qual posição da fruta você quer apagar: "))
            frutas.pop(posicao -1)
        case 0:
            break
        case _:
            print("Opção Inválida")


    # if menu == 1:
    #     frutas.pop()
    # elif menu == 2:
    #     print(frutas)
    #     posicao = int(input("Qual posição da fruta você quer apagar: "))
    #     frutas.pop(posicao -1)
    # elif menu == 0:
    #     break
    # else:
    #     print("Opção Inválida")
