# O loop for é utilizado para iterar sobre os itens de qualquer sequência, como listas, strings, ou objetos de dicionário, e executar um bloco de código para cada item. É especialmente útil quando você precisa executar uma operação para cada elemento de uma coleção.

# O comando for em Python é um pouco diferente do que costuma ser em C ou Pascal. Ao invés de sempre iterar sobre uma progressão aritmética de números (como no Pascal), ou permitir ao usuário definir o passo de iteração e a condição de parada (como C), o comando for do Python itera sobre os itens de qualquer sequência (seja uma lista ou uma string), na ordem que aparecem na sequência. Por exemplo:

# palavras = ['gato', 'cachorro', 'janela']

# for palavra in palavras:
#     print(palavra, len(palavra))

# for i in range(5):
#     print(i)


# list(range(5, 10))


# list(range(0, 10, 3))


# list(range(-10, -100, -30))

# # Contagem de Palavras em Textos
# # Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])


# #Normalização de Dados
# # Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# print(normalizados)



# # Filtragem de Dados Faltantes
# # Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.
# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuarios_validos = [usuario for usuario in usuarios if usuario["email"]]

# print(usuarios_validos)



# # Extração de Subconjuntos de Dados
# # Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

# numeros = range(1, 11)
# pares = [x for x in numeros if x % 2 == 0]

# print(pares)



# # Agregação de Dados por Categoria
# # Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.

# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# total_por_categoria = {}
# for venda in vendas:
#     categoria = venda["categoria"]
#     valor = venda["valor"]
#     if categoria in total_por_categoria:
#         total_por_categoria[categoria] += valor
#     else:
#         total_por_categoria[categoria] = valor

# print(total_por_categoria)

