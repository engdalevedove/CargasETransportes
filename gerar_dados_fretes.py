import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
from datetime import datetime, timedelta

# Função para gerar dados de fretes simulados


def gerar_dados_fretes(num_linhas=1000):
    # Listas de cidades, tipos de carga, formas de pagamento e status de entrega
    cidades = ['São Paulo', 'Belo Horizonte', 'Porto Alegre', 'Fortaleza', 'Manaus',
               'Salvador', 'Curitiba', 'Recife', 'Belém', 'Rio de Janeiro', 'Brasília']
    tipos_carga = ['Eletrônicos', 'Alimentos',
                   'Produtos Químicos', 'Roupas', 'Livros', 'Medicamentos']
    formas_pagamento = ['Cartão de Crédito',
                        'Transferência Bancária', 'Fatura', 'Boleto']
    status_entrega = ['Entregue', 'Atraso']

    # Dicionário para armazenar os dados gerados
    data = {
        # Escolhe uma cidade de origem aleatória para cada linha
        'Origem': [random.choice(cidades) for _ in range(num_linhas)],
        # Escolhe uma cidade de destino aleatória para cada linha
        'Destino': [random.choice(cidades) for _ in range(num_linhas)],
        # Escolhe um tipo de carga aleatório para cada linha
        'Tipo de Carga': [random.choice(tipos_carga) for _ in range(num_linhas)],
        # Gera um valor de frete aleatório entre 500 e 5000
        'Valor do Frete (R$)': [random.randint(500, 5000) for _ in range(num_linhas)],
        # Gera uma data de contratação aleatória em 2023
        'Data de Contratação': [(datetime(2023, 1, 1) + timedelta(days=random.randint(0, 364))).strftime('%Y-%m-%d') for _ in range(num_linhas)],
        # Gera uma data de entrega aleatória
        'Data de Entrega': [(datetime(2023, 1, 1) + timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d') for _ in range(num_linhas)],
        # Gera um tempo de entrega aleatório entre 1 e 15 dias
        'Tempo de Entrega (dias)': [random.randint(1, 15) for _ in range(num_linhas)],
        # Escolhe uma forma de pagamento aleatória
        'Forma de Pagamento': [random.choice(formas_pagamento) for _ in range(num_linhas)],
        # Escolhe um status de entrega aleatório
        'Status da Entrega': [random.choice(status_entrega) for _ in range(num_linhas)],
        # Gera um custo adicional aleatório entre 0 e 200
        'Custo Adicional (R$)': [random.randint(0, 200) for _ in range(num_linhas)],
        # Deixa a coluna de observações vazia
        'Observações': ['' for _ in range(num_linhas)]
    }

    return pd.DataFrame(data)  # Retorna um DataFrame com os dados gerados


# Gerar os dados
df = gerar_dados_fretes(num_linhas=1000)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('amostra_fretes.csv', index=False)

# Análise de Desempenho dos Fretes

# Identificação de Padrões de Atrasos
atrasos = df[df['Status da Entrega'] == 'Atraso']
cidades_com_mais_atrasos = atrasos['Origem'].value_counts()
tipos_carga_com_mais_atrasos = atrasos['Tipo de Carga'].value_counts()

# Análise de Custos Adicionais
custo_adicional_por_cidade = df.groupby(
    'Origem')['Custo Adicional (R$)'].mean()
custo_adicional_por_tipo_carga = df.groupby(
    'Tipo de Carga')['Custo Adicional (R$)'].mean()

# Visualizações

# Gráfico de barras: Número de fretes por cidade de origem
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Origem', order=df['Origem'].value_counts().index)
plt.title('Número de Fretes por Cidade de Origem')
plt.xticks(rotation=45)
plt.savefig('numero_fretes_por_origem.png')
plt.close()

# Mapa de calor: Fretes entre cidades
pivot_table = df.pivot_table(index='Origem', columns='Destino',
                             values='Valor do Frete (R$)', aggfunc='count', fill_value=0)
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
plt.title('Mapa de Calor de Fretes entre Cidades')
plt.savefig('mapa_calor_fretes.png')
plt.close()

# Linha do tempo: Fretes ao longo do tempo
df['Data de Contratação'] = pd.to_datetime(df['Data de Contratação'])
fretes_por_data = df.groupby(
    df['Data de Contratação'].dt.to_period('M')).size()
fretes_por_data.index = fretes_por_data.index.to_timestamp()

plt.figure(figsize=(10, 6))
fretes_por_data.plot()
plt.title('Número de Fretes ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Número de Fretes')
plt.grid(True)
plt.savefig('fretes_ao_longo_tempo.png')
plt.close()

# Visualização de atrasos por cidade de origem
plt.figure(figsize=(10, 6))
cidades_com_mais_atrasos.plot(kind='bar')
plt.title('Número de Atrasos por Cidade de Origem')
plt.ylabel('Número de Atrasos')
plt.xlabel('Cidade de Origem')
plt.savefig('atrasos_por_cidade.png')
plt.close()

# Visualização de atrasos por tipo de carga
plt.figure(figsize=(10, 6))
tipos_carga_com_mais_atrasos.plot(kind='bar')
plt.title('Número de Atrasos por Tipo de Carga')
plt.ylabel('Número de Atrasos')
plt.xlabel('Tipo de Carga')
plt.savefig('atrasos_por_tipo_carga.png')
plt.close()

# Visualização de custos adicionais por cidade de origem
plt.figure(figsize=(10, 6))
custo_adicional_por_cidade.plot(kind='bar')
plt.title('Custo Adicional Médio por Cidade de Origem')
plt.ylabel('Custo Adicional Médio (R$)')
plt.xlabel('Cidade de Origem')
plt.savefig('custo_adicional_por_cidade.png')
plt.close()

# Visualização de custos adicionais por tipo de carga
plt.figure(figsize=(10, 6))
custo_adicional_por_tipo_carga.plot(kind='bar')
plt.title('Custo Adicional Médio por Tipo de Carga')
plt.ylabel('Custo Adicional Médio (R$)')
plt.xlabel('Tipo de Carga')
plt.savefig('custo_adicional_por_tipo_carga.png')
plt.close()

# Recomendações
recomendacoes = """
1. Focar em melhorar as operações logísticas nas cidades com maior número de atrasos.
2. Implementar processos específicos para tipos de carga que frequentemente sofrem atrasos.
3. Analisar os fatores que contribuem para altos custos adicionais em determinadas cidades e tipos de carga e buscar soluções para minimizá-los.
"""

with open('recomendacoes.txt', 'w') as f:
    f.write(recomendacoes)

print("Análise de desempenho e recomendações geradas e salvas como imagens e texto.")
