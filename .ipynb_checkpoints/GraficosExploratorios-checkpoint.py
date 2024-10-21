import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_pdf import PdfPages

# Carregar o conjunto de dados
dados = pd.read_csv("/Users/pedrosof/Documents/FIAP/Trabalhos/Fase3_Cap14/Atividade_Cap_14_produtos_agricolas.csv")

# Criar um arquivo PDF para salvar os gráficos
with PdfPages('analise_produtos_agricolas.pdf') as pdf:
    
    # Distribuição de Nitrogênio (N)
    plt.figure(figsize=(8,6))
    sns.histplot(dados['N'], bins=10, kde=False, color="blue")
    plt.title('Distribuição de Nitrogênio (N)')
    plt.xlabel('Nível de Nitrogênio')
    plt.ylabel('Contagem')
    pdf.savefig()  # Salva o gráfico no PDF
    plt.close()
    
    # Distribuição de Fósforo (P)
    plt.figure(figsize=(8,6))
    sns.histplot(dados['P'], bins=10, kde=False, color="green")
    plt.title('Distribuição de Fósforo (P)')
    plt.xlabel('Nível de Fósforo')
    plt.ylabel('Contagem')
    pdf.savefig()  # Salva o gráfico no PDF
    plt.close()
    
    # Distribuição de Potássio (K)
    plt.figure(figsize=(8,6))
    sns.histplot(dados['K'], bins=10, kde=False, color="red")
    plt.title('Distribuição de Potássio (K)')
    plt.xlabel('Nível de Potássio')
    plt.ylabel('Contagem')
    pdf.savefig()  # Salva o gráfico no PDF
    plt.close()
    
    # Distribuição dos Níveis de pH
    plt.figure(figsize=(8,6))
    sns.histplot(dados['ph'], bins=10, kde=False, color="purple")
    plt.title('Distribuição dos Níveis de pH')
    plt.xlabel('Nível de pH')
    plt.ylabel('Contagem')
    pdf.savefig()  # Salva o gráfico no PDF
    plt.close()

    # Distribuição da Precipitação
    plt.figure(figsize=(8,6))
    sns.histplot(dados['rainfall'], bins=10, kde=False, color="cyan")
    plt.title('Distribuição da Precipitação')
    plt.xlabel('Precipitação (mm)')
    plt.ylabel('Contagem')
    pdf.savefig()  # Salva o gráfico no PDF
    plt.close()

    # Relação entre Nitrogênio e Fósforo
    plt.figure(figsize=(8,6))
    sns.scatterplot(x=dados['N'], y=dados['P'], color="blue")
    plt.title('Relação entre Nitrogênio e Fósforo')
    plt.xlabel('Nitrogênio (N)')
    plt.ylabel('Fósforo (P)')
    pdf.savefig()  # Salva o gráfico no PDF
    plt.close()

    # Relação entre Temperatura e Umidade
    plt.figure(figsize=(8,6))
    sns.scatterplot(x=dados['temperature'], y=dados['humidity'], color="red")
    plt.title('Relação entre Temperatura e Umidade')
    plt.xlabel('Temperatura (°C)')
    plt.ylabel('Umidade (%)')
    pdf.savefig()  # Salva o gráfico no PDF
    plt.close()

    # Distribuição dos Tipos de Cultura
    plt.figure(figsize=(8,6))
    sns.countplot(x=dados['label'], color="orange")  # Usar a cor laranja para todos
    plt.title('Distribuição dos Tipos de Cultura')
    plt.xlabel('Tipo de Cultura')
    plt.ylabel('Contagem')
    pdf.savefig()  # Salva o gráfico no PDF
    plt.close()

    # Matriz de Correlação
    variaveis_correlacao = dados[['N', 'P', 'K', 'temperature', 'humidity', 'rainfall']]
    cor_matrix = variaveis_correlacao.corr().round(2)

    plt.figure(figsize=(10,8))
    sns.heatmap(cor_matrix, annot=True, cmap="coolwarm", center=0, linewidths=.5)
    plt.title("Matriz de Correlação entre Variáveis")
    pdf.savefig()  # Salva o gráfico no PDF
    plt.close()

print("Gráficos salvos no arquivo analise_produtos_agricolas.pdf")
