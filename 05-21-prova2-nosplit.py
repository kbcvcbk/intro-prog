'''
## Questão 2 da 2a Avaliação sem usar `.split()` ##
# by Kalil

    O loop nessa questão vai adicionando caractere por caractere da string
"letra" à string "palavra" até encontrar um caractere " " (espaço). Quando
isso acontece, o programa verifica se a palavra é uma substring de "saida",
e, caso não seja, adiciona a palavra à string "saida".
    Importante notar que é necessário adicionar um espaço no fim da string
pois caso contrário o programa irá ignorar a última palavra.
'''
# inicialização
entrada = "like Baby baby baby ohhh Baby baby Like nooo"
palavra = ""
saida = ""

# formatando a entrada
letra = entrada.lower()+" "

# loop principal
i=0
while i < len(letra):
    char = letra[i]
    if char != " ":     # se char não for um espaço...
        palavra += char # adicione char a palavra
    else:
        # aqui eu sei que cheguei no fim de uma palavra
        if not (palavra in saida):  # caso palavra NÃO esteja dentro de saida
            saida += palavra+" "    # adicione "palavra"+" " a saida
        palavra = "" # limpa a string palavra pra poder começar de novo

# resultado
saida = saida.strip()
print(saida)
