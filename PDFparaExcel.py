import pdfplumber
import pandas as pd

# Função para extrair dados do PDF
def extrair_dados_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        texto = ""
        # Iterar por todas as páginas do PDF e extrair o texto
        for pagina in pdf.pages:
            texto += pagina.extract_text()

    return texto

# Função para processar o texto extraído e convertê-lo em uma tabela
def processar_dados_para_tabela(texto):
    linhas = texto.split("\n")
    dados = []

    # Vamos percorrer as linhas e tentar organizar as informações conforme as colunas desejadas
    for linha in linhas:
        partes = linha.split()  # Divida a linha em partes separadas por espaços

        # Verifique se a linha contém o número esperado de colunas
        if len(partes) >= 8:  # Ajuste conforme necessário
            cargo = partes[0]  # O cargo será a primeira palavra
            nome_candidato = " ".join(partes[1:-6])  # O nome será o que vem entre o cargo e as notas
            nota = partes[-6]  # A nota é o 6º valor a partir do final
            obj = partes[-5]
            lp = partes[-4]
            mat = partes[-3]
            cg = partes[-2]
            ce = partes[-1]  # O último valor será o CE

            dados.append([cargo, nome_candidato, nota, obj, lp, mat, cg, ce])

    # Converter a lista de dados para um DataFrame com os nomes das colunas
    df = pd.DataFrame(dados, columns=["Cargo", "Nome Candidato(a)", "Nota", "Obj", "LP", "MAT", "CG", "CE"])
    return df

# Função para salvar o DataFrame em um arquivo Excel
def salvar_como_excel(df, output_path):
    # Salvar o DataFrame no formato Excel
    df.to_excel(output_path, index=False)
    print(f"Dados salvos em {output_path}")

# Caminho do arquivo PDF
pdf_path = 'Departamento de Administração.pdf'  # Substitua pelo caminho do seu PDF

# Extração de dados do PDF
texto = extrair_dados_pdf(pdf_path)

# Processamento dos dados
df = processar_dados_para_tabela(texto)

# Verifique as primeiras linhas para depuração
print("Primeiras linhas do DataFrame:")
print(df.head())  # Verifique as primeiras linhas para confirmar a extração correta

# Salvar os dados em um arquivo Excel
output_path = 'resultado_dados_tabela.xlsx'  # Caminho para salvar o arquivo Excel
salvar_como_excel(df, output_path)
