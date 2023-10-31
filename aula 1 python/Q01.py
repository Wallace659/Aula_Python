# Escreva um programa que solicite ao usuário um número inteiro positivo
# e realize uma contagem regressiva a partir desse número até Zero,
# imprimindo cada número no processo.


numero = int(input("Digite um número: "))

#exemplo 1
while numero >=0:
    print(numero)
    numero -= 1

#exemplo 2    
for i in range(numero, -1, -1):
    print(i)
