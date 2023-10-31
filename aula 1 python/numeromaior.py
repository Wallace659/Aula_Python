# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO ESCREVER 3 NÚMEROS
# INTEIROS E MOSTRE NA TELA QUAL É O MAIOR DOS 3


n1 = int(input("Digite um numero :"))
n2 = int(input("Digite um numero :"))
n3 = int(input("Digite um numero :"))

if n1 >= n2 and n1 >= n3:
    print(f"o {n1} é o maior")
elif n2 >= n1 and n2 >= n3:
    print(f"o {n2} é o maior")
elif n3 >= n1 and n3 >= n2:
    print(f"o {n3} é o maior")

