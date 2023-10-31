# faça um programa que pede para o usuário escolher uma cor do semaforo: verde , vermelho , amarelo
# "acelere!" caso seja verde
# "atenção!" caso seja amarelo
# "pare!" caso seja vermelho
# "cor invalida" para outras cores


cor = str(input("Digite uma cor do semaforo:"))

if cor == "verde":
    print("acelere")
elif cor == "amarelo":
    print("atenção")
elif cor == "vermelho":
    print("pare")
else:
    print(" cor inválida")

#exemplo 2

cor = str(input("Escolha uma cor do semáforo: ")).lower()

match cor:
    case "vermelho":
        print("Pare!")
    case "amarelo":
        print("Atenção!")
    case "verde":
        print("Acelere!")
    case _:
        print("Cor inválida")

#exemplo 3

cor = int(input("""
                Escolha uma cor do semáforo:
                1 - Vermelho
                2 - Amarelo
                3 - Verde
                 """))
match cor:
    case 1:
        print("Pare!")
    case 2:
        print("Atenção!")
    case 3:
        print("Acelere!")
    case _:
        print("Cor inválida")