# faça um programa que peça dois números ao usuário e imprima o maior deles.

n1 = int(input("Digite um número:"))
n2 = int(input("Digite um número:"))

if n1 > n2:
    print(f"o {n1} é maior.")
elif n2 > n1:
    print(f"O {n2} é maior.")
else:
    print("Os números são iguais")