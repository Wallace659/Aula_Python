# DADO A LISTA: 
# ["UVA", "PÊRA", "MELÃO", "MAÇA", "BANANA", "ACEROLA", "ABACAXI"]
# FAÇA UM PROGRAMA QUE PERGUNTA PRO USUÁRIO QUAL FRUTA ELE QUER EXCLUIR (A POSIÇÃO DA FRUTA) E EXCLUA ELA

frutas = ["UVA", "PÊRA", "MELÃO", "MAÇA", "BANANA", "ACEROLA", "ABACAXI"]

print(frutas)
posicao = int(input("Digite a posição da fruta que você quer excluir: "))
frutas.pop(posicao - 1)

print(frutas)
