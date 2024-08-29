#%%
# palavras = ['gato', 'cachorro', 'janela']

# for palavra in palavras:
#     print(palavra, len(palavra))

# Se você precisa iterar sobre sequências numéricas, a função embutida range() é a resposta. Ela gera progressões aritméticas:

# for i in range(5):
#     print(i)


# '''O ponto de parada fornecido nunca é incluído na lista; range(10) 
# gera uma lista com 10 valores, exatamente os índices válidos 
# para uma sequência de comprimento 10. É possível iniciar o intervalo com
# outro número, ou alterar a razão da progressão (inclusive com passo negativo):'''

# ## range de 5 a 10
# resultado_lista= list(range(5, 10))
# resultado_lista


# ## range de 0 a 10 com intervalo de 3
# resultado_lista_intervalo = list(range(0,10,3))
# resultado_lista_intervalo

# resultado_lista_negativo = list(range(-20, -100, -30))
# resultado_lista_negativo


# '''Para iterar sobre os índices de uma sequência, combine range() e len() da seguinte forma:'''

# lista_palavras = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(lista_palavras)):
#     print(i, lista_palavras[i])


# '''
# Contagem de Palavras em Textos

# Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
# '''
# texto = ' a raposa marrom salta a sobre o cachorro preguiçoso'

# palavras = texto.split()

# contagem_palavras = {}

# for palavra in palavras:
#     if palavra in contagem_palavras:
#         contagem_palavras[palavra] += 1
#     else:
#         contagem_palavras[palavra] = 1

# print(contagem_palavras)

# '''
# Normalização de Dados
# Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# '''
# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)

# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]
# print(normalizados)

'''
Filtragem de Dados Faltantes
Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.
'''
usuarios = [
    {'nome' : 'Alice', 'email' : 'alice@exemplo.com'},
    {'nome' : 'João', 'email' : ''},
    {'nome' : 'Carol', 'email' : 'carol@exemplo.com'}
]

usuarios_validos = [usuario for usuario in usuarios if usuario['email']]

print(usuarios_validos)