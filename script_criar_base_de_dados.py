import pandas as pd
import random
from datetime import datetime, timedelta

# Função para gerar dados de fretes simulados


def gerar_dados_fretes(num_linhas=1000):
    cidades = ['São Paulo', 'Belo Horizonte', 'Porto Alegre', 'Fortaleza', 'Manaus',
               'Salvador', 'Curitiba', 'Recife', 'Belém', 'Rio de Janeiro', 'Brasília']
    tipos_carga = ['Eletrônicos', 'Alimentos',
                   'Produtos Químicos', 'Roupas', 'Livros', 'Medicamentos']
    formas_pagamento = ['Cartão de Crédito',
                        'Transferência Bancária', 'Fatura', 'Boleto']
    status_entrega = ['Entregue', 'Atraso']

    data = {
        'Origem': [random.choice(cidades) for _ in range(num_linhas)],
        'Destino': [random.choice(cidades) for _ in range(num_linhas)],
        'Tipo de Carga': [random.choice(tipos_carga) for _ in range(num_linhas)],
        'Valor do Frete (R$)': [random.randint(500, 5000) for _ in range(num_linhas)],
        'Data de Contratação': [(datetime(2023, 1, 1) + timedelta(days=random.randint(0, 364))).strftime('%Y-%m-%d') for _ in range(num_linhas)],
        'Data de Entrega': [(datetime(2023, 1, 1) + timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d') for _ in range(num_linhas)],
        'Tempo de Entrega (dias)': [random.randint(1, 15) for _ in range(num_linhas)],
        'Forma de Pagamento': [random.choice(formas_pagamento) for _ in range(num_linhas)],
        'Status da Entrega': [random.choice(status_entrega) for _ in range(num_linhas)],
        'Custo Adicional (R$)': [random.randint(0, 200) for _ in range(num_linhas)],
        'Observações': ['' for _ in range(num_linhas)]
    }

    return pd.DataFrame(data)


# Gerar dados com mais de 1000 linhas
df = gerar_dados_fretes(num_linhas=1000)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('amostra_fretes.csv', index=False)

print("Arquivo 'amostra_fretes.csv' criado com sucesso!")
