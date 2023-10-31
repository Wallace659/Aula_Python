# faça um programa para a  leitura de quatro notas de um aluno.
# O programa deve calcular a média alcançada apresentar:
# a. A mensagem "aprovado", se a média alcançada for maior ou igual a sete.
# b. A mensagem "Reprovado", se a média for menor do que sete.
# c. A mensagem "Aprovado com distinção", se a média for igual a dez.


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7 and media < 10:
    print("Aprovado")
elif media < 7 and media >= 0:
    print("Reprovado")
elif media == 10:
    print("Aprovado com distinção")
else:
    print("Média inválida, digite notas entre 0 e 10")


#questão ainda aprensenta erro exemplo 20 + 0 + 4 + 8 ainda vai sair uma media dentro de aprovado porém so pode ser aceito valores entre 0 e 10.
