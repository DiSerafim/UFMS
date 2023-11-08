import pandas as pd
import csv
import matplotlib.pyplot as plt
import json
import requests

# Abre o documento de texto ------------------------------- TXT
arquivo = open('0-modulo2_unidade_2_v1-arquivos.txt', 'r')

# Ler as linhas do arquivo
conteudo = arquivo.readlines()
arquivo.close()

print(conteudo)

# exibe linha por linha
for linha in conteudo:
    print(linha)

x = ''
for linha in conteudo:
    if linha != '':
        x += linha

print(x)

# altera as palavras
x = x.replace('Gravar Dados / Demonstração', 'Demonstração / Gravar Dados')
print('----------')
print(x)

# Grava e gera um novo arquivo
arquivo_novo = open('0-modulo2_unidade_2_v1-arquivos2.txt', 'w')
arquivo_novo.writelines(x)
arquivo_novo.close()

# Abrindo arquivo CSV ------------------------------- CSV
with open('0-modulo2_unidade_2_v1-arquivos.csv', 'r') as f:
    leitor = csv.reader(f, delimiter = ',')
    for linha in leitor:
        data = linha[0]
        fechamento = linha[4]
        volume = linha[5]
        print('Data: ', data, '--Fechamento: ', fechamento, '--Volume: ', volume)

# Plotar gráficos em Python, uma das bibliotecas mais populares é o matplotlib
# Dados de exemplo
x = [1, 2, 3, 4, 5]
y = [10, 8, 6, 4, 2]

# Cria o gráfico de dispersão
plt.scatter(x, y)

# Adiciona rótulos aos eixos
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Título do gráfico
plt.title('Gráfico de Dispersão')

# Mostra o gráfico
plt.show()

# Plotar Python
# Abra o arquivo para leitura
with open("0-modulo2_unidade_2_v1-arquivos.txt", "r") as arquivo:
    # Use o método readlines() para ler todas as linhas do arquivo em uma lista
    linhas = arquivo.readlines()

# Use a função len() para contar as linhas
numero_de_linhas = len(linhas)

# Imprima o número de linhas
print(f"O arquivo tem {numero_de_linhas} linhas.")

# Abrindo arquivo JSON ------------------------------- JSON
resposta = requests.get('https://storage.googleapis.com/kagglesdsdata/datasets/2394309/4042051/Data.json?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20231108%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20231108T005815Z&X-Goog-Expires=259200&X-Goog-SignedHeaders=host&X-Goog-Signature=2ed165dcae6e34831cd428b58dc539428dabb5a3a6d52d52ce1c40acbcbd2960d10a1fd8feecf83bae58914d4d56ed46b3bf4f812346448b42f14ae980b97e0548e1752c815e88097ff504a4e74c686d5ef2e1ed009c04197d28912c0d3f85ed87c87d7f2ea2434e1624bd9483bfc3eb880ddb9db8a9d1580671ccb2acdb49a77d238dfdc78e8e6bf347b39ee0a741643acc5e7af1899ad4317e74de0d3e34cb3e696731e6ef4f5d83bdbc6bea72872befd92fd15966b69a8d8c091238bed3ab16bdcead85e7d7743147a46bbc1e6c77797cbd8f554844a19c459054cdb1b38c5e3dd193a5e95071de318dde8dbbf2f9b06b288e39c309c1a5b1e1792ad03237')
# resposta = '0-modulo2_unidade_2_v1-arquivos.json'
dados = json.loads(resposta.text)
print(dados['XMax'])
