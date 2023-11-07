# Faça um programa que pede para o usuario digitar 5 frutas
# e adicionar as 5 frutas na lista de frutas
# ["Uva", "Pêra", "Melão"]

lista = ["Uva", "Pêra", "Melão"]

fruta1 = str(input("Digite uma fruta:"))
lista.append(fruta1)
fruta2 = str(input("Digite uma fruta:"))
lista.append(fruta2)
fruta3 = str(input("Digite uma fruta:"))
lista.append(fruta3)
fruta4 = str(input("Digite uma fruta:"))
lista.append(fruta4)
fruta5 = str(input("Digite uma fruta:"))
lista.append(fruta5)

print(lista)


#exemplo 2

lista_fruta = ["Uva","Pêra", "Melão"]
qtde_fruta = int(input("Quantas frutas voçê quer adicionar? :"))
for i in range(qtde_fruta):
    fruta = str(input("Digite uma fruta:"))
    lista_fruta.append(fruta)

print(lista_fruta)
