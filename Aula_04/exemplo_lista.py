import json

nome: str = 'Televisao'
valor: float = 120.10
quantidade: int = 20

# Criando uma lista
produtos: list = []

# Adiciona produtos
produtos.append(nome)
produtos.append(valor)
produtos.append(quantidade)

print(produtos)
#Remove o ultimo item da lista
# produtos.pop()

#Remove um item da sua escolha
# produtos.remove(nome)

## Exemplo de dicionario

produto_01: dict = {
    'Nome' : nome,
    'Valor': valor,
    'Quantidade' : quantidade
}

produto_02: dict = {
    'Nome' : 'Controle',
    'Valor' : 10,
    'Quantidade' : 2
}

# Exemplo de uma lista de dicionarios
carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)
print(carrinho)


## Exemplo de Json 
carrinho_json = json.dumps(carrinho)
print(f'Json: {carrinho_json}')