# faça um programa que peça ao usuário um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input("Digite um número:"))

if numero > 0:
    print("Positivo")
elif numero < 0:
    print("Negativo")
else:
    print("Neutro")