dicionario = {
    "Módulo": "Python",
    "Instituição": "Infinity School"
}

print(list(dicionario))
print(len(dicionario))
print(dicionario["instituição"])

dicionario["Módulo"] = "Javascript" # substitui um item
print(dicionario)
dicionario["Lugar"] = "Plaza Tower" # se não tiver o item no dicionario ele adiciona

del dicionario["Instituição"] # retira a chave e valor

print(dicionario)

print("Módulo" in dicionario) # uma pergunta de verificação

lista = ["nome", "idade", "altura"]

print(dict.fromkeys(lista))  # cria um dicionario da lista

print(dicionario.get("Módulo", "Chave não encontrada.")) # função get busca o valor e pode escrever uma mensagem.

print(dicionario.pop("Módulo", "Chave não encontrada.")) # deleta uma chave e nao quebra o codigo

dicionario.update({

})   # esse comando add um dicionario e atualiza o anterior






