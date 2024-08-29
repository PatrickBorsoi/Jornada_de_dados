import time
# # Exemplo Prático: while True com Pausa
# while True:
#     print('Verificando novos dados')


#     time.sleep(10)


# Leitura de Dados até Flag
# Objetivo: Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

#%%
palavra =''
while palavra.lower() != 'sair':
    palavra = input('Digite uma palavra: ').lower()

 #%%
numero = int(input('Digite um número entre 1 e 10: '))

while numero < 1 or numero > 10:
    print(f'Número {numero} fora do intervalo!')
    numero = int(input('Digite um número entre 1 e 10: '))

print('Numero Valido')


# %%
# Consumo de API Simulado
# Objetivo: Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.

pagina_inicial = 1
pagina_fim = 6

while pagina_inicial <= pagina_fim:
    print(f'Pagina atual {pagina_inicial} de {pagina_fim}')

    pagina_inicial += 1

print('Todas as paginas foram lidas')

#%%
# Tentativas de Conexão
# Objetivo: Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

tentativas_maximas = 5
tentativa = 1

while tentativa <= tentativas_maximas:
    print(f"Tentativa {tentativa} de {tentativas_maximas}")
    # Simulação de uma tentativa de conexão
    # Aqui iria o código para tentar conectar
    if False:  # Suponha que a conexão foi bem-sucedida
        print("Conexão bem-sucedida!")
        break
    tentativa += 1
else:
    print("Falha ao conectar após várias tentativas.")

#%%
#     Processamento de Dados com Condição de Parada
# Objetivo: Processar itens de uma lista até encontrar um valor específico que indica a parada.

lista_n = [1,4,5,2,6,"parar",7,4,8]
i=0
while i < len(lista_n):
    if lista_n[i] == "parar":
        print('Parada encontrada, encerrando processamento')
        break
    print(f'Processando item: {lista_n[i]}')
    i += 1

#Desafio
# %%
#Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas
nome_valido = False
salario_valido = False
bonus_valido = False

#loop para verificar o nome
while not nome_valido:
    try:
        nome = input('Digite seu nome: ')
        if len(nome) == 0:
            raise ValueError('O nome não pode estar vazio.')
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print('Nome válido', nome)
            nome_valido = True
    except ValueError as e:
        print(e)

# loop para verificar salario_valido
while not salario_valido:
    try:
        salario = float(input("Digite seu salario: "))
        if salario < 0:
            print('Por favor, digite um valor positivo para o salário.')
        else:
            salario_valido = True
    except ValueError:
        print('Entrada inválida para o salário. Porfavor, digite um número.')
# loop para verificar bonus
while not bonus_valido:
    try:
        bonus = float(input('Digite o valor do bônus recebido: '))
        if bonus < 0:
            print('Por favor, digite um valor positivo para o bônus.')
        else:
            bonus_valido = True
    except ValueError:
        print('Entrada inválida para o bônus')
bonus_recebido = 1000 + salario * bonus

print(f"{nome}, seu salário é R${salario:.2f} e seu bônus final é R${bonus_recebido:.2f}.")
# %%
