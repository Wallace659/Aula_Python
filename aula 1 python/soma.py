# faça um programa que pede para o usuário digitar 5 números
# e no final mostrar a soma dos 5 números digitados
# usando o for

soma = 0
for i in range(1,6):
    numero = int(input(f"Digite o {i}° número: "))
    soma = soma + numero

print(f"A soma dos valores foi: {soma}")

