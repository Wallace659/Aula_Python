# faça um programa que imprima na tela "feminino", "masculino" ou "sexo inválido" 
# a partir de uma letra digitada: F ou f para feminino, M ou m para masculino e qualquer outra letra para sexo inválido.

# codigo len servi para limitar quantidade de letra
# .upper() letras maiusculas .strip() tira os espaços


letra = str(input("""
                  Digite uma letra:
                  F - Feminino
                  M - Masculino
                   """)).upper().strip()

if len(letra) == 1:
    match letra:
        case "F":
            print("Sexo Feminino")
        case "M":
            print("Sexo Masculino")
        case _:
            print("Sexo inválido")
else:
    print("Digite apenas uma letra")

# o _ no case é a mesma coisa que o else .

