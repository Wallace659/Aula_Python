# faça um programa que verifique se a letra digitada pelo usuário é vogal ou consoante.

letra = str(input("Digite uma letra: ")).lower().strip()

if len(letra) == 1:
    if letra in "aeiou":
        print(f"A '{letra}' é uma vogal")
    elif letra in "bcdfghjklmnpqrstvxywz":
        print(f"A '{letra}' é uma consoante")
    else:
        print(f"Você digitou '{letra}' por favor digite uma letra do alfabeto")

else:
    print("Digite apenas uma letra")