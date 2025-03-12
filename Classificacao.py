import pandas as pd

# Função para ler o arquivo Excel
def ler_arquivo_excel(caminho_arquivo):
    # Ler o arquivo Excel
    df = pd.read_excel(caminho_arquivo)
    return df

# Função para processar as colunas e calcular a média
def calcular_media_e_classificar(df):
    # Remover espaços extras nos nomes das colunas
    df.columns = df.columns.str.strip()

    # Verificar os nomes das colunas
    print("Colunas disponíveis no DataFrame:")
    print(df.columns)

    # Verificar se as colunas necessárias estão presentes
    colunas_necessarias = ['Nota', 'LP', 'MAT', 'CG', 'CE']
    for coluna in colunas_necessarias:
        if coluna not in df.columns:
            raise KeyError(f"A coluna '{coluna}' não foi encontrada no DataFrame.")

    # Calcular a média dos campos NotaObj, LP, MAT, CG, CE
    df['Média'] = df[['Nota', 'LP', 'MAT', 'CG', 'CE']].mean(axis=1)
    
    # Ordenar os dados pela média em ordem decrescente (do maior para o menor)
    df_sorted = df.sort_values(by='Média', ascending=False)
    
    # Adicionar a coluna de colocação, baseada na ordem dos dados
    df_sorted['Colocação'] = range(1, len(df_sorted) + 1)
    
    return df_sorted

# Função para salvar o DataFrame com a média e colocação em um novo arquivo Excel
def salvar_como_excel(df, output_path):
    # Salvar o DataFrame no formato Excel
    df.to_excel(output_path, index=False)
    print(f"Dados salvos em {output_path}")

# Caminho do arquivo Excel (substitua com o caminho do seu arquivo)
caminho_arquivo = 'dados_modificado.xlsx'  # Substitua pelo caminho do seu arquivo Excel

# Ler os dados do arquivo Excel
df = ler_arquivo_excel(caminho_arquivo)

# Verificar as primeiras linhas do arquivo para ver se a leitura foi correta
print("Primeiras linhas do arquivo:")
print(df.head())

# Calcular a média, classificar e adicionar a coluna de colocação
df_classificado = calcular_media_e_classificar(df)

# Verificar as primeiras linhas após o processamento
print("Primeiras linhas após calcular a média e classificar:")
print(df_classificado.head())

# Caminho para salvar o arquivo Excel com a média e a classificação
output_path = 'dados_classificados.xlsx'  # Caminho para salvar o arquivo Excel
salvar_como_excel(df_classificado, output_path)

