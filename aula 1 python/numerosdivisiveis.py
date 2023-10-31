# faça um programa que mostre os números de 5 até 50 na tela
# faça um programa que mostre os números de 10 a 100, porém
# apenas os que forem divisíveis por 3 e 5 ao mesmo tempo.


for i in range(5,51):
    print(i)


for i in range(10,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)