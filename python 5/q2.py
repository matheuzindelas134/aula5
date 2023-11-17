def maior_palavra(lista_de_palavras):
    maior = ""
    for item_da_vez in lista_de_palavras:
        if len(item_da_vez) > len(maior):
            maior = item_da_vez
    return maior
quantidade = int(input("digite quantas palavras voce quer inserir: "))

lista_de_nome = []

for i in range(quantidade):
    nome = str(input("digite uma palavra: "))
    lista_de_nome.append(nome)

maior = maior_palavra(lista_de_nome)

print(f"A maior palavra foi: {maior}")