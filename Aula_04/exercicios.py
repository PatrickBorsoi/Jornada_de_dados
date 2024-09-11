# Crie uma estrutura de dados para armazenar informações de um livro
# incluindo título, autor e ano da publicação. Imprima cada informação
from typing import Dict, Any

livro_01: Dict[str, Any] = {
    'nome': 'Fundamentos de Engenharia de Dados',
    'autor': 'Joe Reis',
    'ano': 2023,
}

livro_02: Dict[str, Any] = {
    'nome': 'Data Science do Zero: Primeiras Regras com o Python',
    'autor': 'Joel Grus',
    'ano': 2015
}

# lista de dicionarios
lista_de_livros: list = []
lista_de_livros.append(livro_01)
lista_de_livros.append(livro_02)
# print(lista_de_livros)

# Imprimindo cada elemento da lista
for chave, valor in livro_01.items():
    print(f'{chave}: {valor}')

lista_de_livros_usando_dict: dict = {
    'livro_01': {
        'titulo': 'Fundamentos de Engenharia de Dados',
        'autor': 'Joe Reis',
        'ano': 2023,
    },
    'livro_02': {
        'titulo': 'Data Science do Zero: Primeiras Regras com o Python',
        'autor': 'Joel Grus',
        'ano': 2015
    }
}
# Lendo a lista de dicionarios
# print(lista_de_livros_usando_dict['livro_01'])
# print(lista_de_livros_usando_dict['livro_01']['nome'])






