#%%
### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
produto : str = input('Digite seu produto ')
quantidade : int = int(input('Qual a quantidade '))
preco : float = float(input('Digite o preço do produto '))

if produto and quantidade and preco < 0:
    print('Dados invalidos')
else:
    print(f'Dados validos, Seu produto {produto} tem essa quantidade {quantidade} e esse preço {preco}')
### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
#%%
temperatura:float = float(input("Digite sua temperatura"))

try:
    if temperatura >= 36 and temperatura <= 37.5:
        print('Sua temperatura esta normal')
    elif temperatura >= 37.6 and temperatura <= 39.5:
        print('Você esta com febre')
    elif temperatura >= 39.6:
        print('Você esta com febre muito alta')
    else:
        print('Sua temperatura esta baixa')
except Exception as e:
    print(e)


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
#%%
from datetime import datetime
data_atual = datetime.now()

log = {
    'timeStamp': data_atual,
    'level' : 'ERROR',
    'message' : 'Falha na conexão'
}

if log['level'] == 'ERROR':
    print(log['message'])



### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
#%%
idade_valida : int = int(input('Qual é a sua idade '))
email_valido : str = input('Digite seu E-mail ')

if idade_valida <= 18 and idade_valida >= 65:
    print('Idade invalida')
elif "@" not in email_valido or "." not in email_valido:
    print('Email inválido')
else:
    print('Dados válidos')



### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

transicao = {
    'valor' : 12000,
    'hora' : 20
}

if transicao['valor'] > 10000:
    print(f'Transação de {transicao["valor"]}, transação suspeita"')
elif transicao['hora'] < 9 or transicao['hora'] > 18:
    print(f'Transação as {transicao["hora"]}, transação suspeita"')
else:
    print('Transação aceita')

# %%