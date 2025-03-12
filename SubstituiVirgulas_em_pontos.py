import pandas as pd

# Função para ler e substituir vírgulas por pontos
def substituir_virgulas_por_pontos(caminho_arquivo):
    # Ler o arquivo Excel
    df = pd.read_excel(caminho_arquivo)

    # Substituir todas as vírgulas por pontos em todo o DataFrame
    df = df.applymap(lambda x: str(x).replace(',', '.') if isinstance(x, str) else x)

    # Verificar as primeiras linhas do arquivo após a modificação
    print("Primeiras linhas após substituir vírgulas por pontos:")
    print(df.head())

    # Salvar o DataFrame modificado em um novo arquivo Excel
    novo_caminho = caminho_arquivo.replace('.xlsx', '_modificado.xlsx')
    df.to_excel(novo_caminho, index=False)
    print(f"Novo arquivo salvo em: {novo_caminho}")

# Caminho do arquivo Excel (substitua com o caminho do seu arquivo)
caminho_arquivo = 'dados.xlsx'  # Substitua pelo caminho do seu arquivo Excel

# Chamar a função para substituir as vírgulas por pontos
substituir_virgulas_por_pontos(caminho_arquivo)
