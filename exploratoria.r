# Carregar as bibliotecas necessárias
library(ggplot2)
library(dplyr)
library(corrplot)

# Carregar o conjunto de dados (substitua o caminho do arquivo)
df <- read.csv("caminho_do_arquivo.csv")

# 1. Análise Exploratória de Dados (EDA)
# Visualizar as estatísticas básicas do conjunto de dados
summary(df)

# 2. Visualizações com histogramas
# Histograma para Nitrogênio (N)
ggplot(df, aes(x = N)) +
  geom_histogram(aes(y = ..density..), bins = 30, fill = "skyblue", color = "black") +
  geom_density(color = "red") +
  ggtitle("Distribuição de Nitrogênio (N)")

# Histograma para Fósforo (P)
ggplot(df, aes(x = P)) +
  geom_histogram(aes(y = ..density..), bins = 30, fill = "skyblue", color = "black") +
  geom_density(color = "red") +
  ggtitle("Distribuição de Fósforo (P)")

# Histograma para Potássio (K)
ggplot(df, aes(x = K)) +
  geom_histogram(aes(y = ..density..), bins = 30, fill = "skyblue", color = "black") +
  geom_density(color = "red") +
  ggtitle("Distribuição de Potássio (K)")

# Histograma para Temperatura
ggplot(df, aes(x = temperature)) +
  geom_histogram(aes(y = ..density..), bins = 30, fill = "skyblue", color = "black") +
  geom_density(color = "red") +
  ggtitle("Distribuição de Temperatura")

# Histograma para Umidade
ggplot(df, aes(x = humidity)) +
  geom_histogram(aes(y = ..density..), bins = 30, fill = "skyblue", color = "black") +
  geom_density(color = "red") +
  ggtitle("Distribuição de Umidade")

# Histograma para Precipitação
ggplot(df, aes(x = rainfall)) +
  geom_histogram(aes(y = ..density..), bins = 30, fill = "skyblue", color = "black") +
  geom_density(color = "red") +
  ggtitle("Distribuição de Precipitação")

# 3. Boxplots para visualização de outliers
# Boxplot para Nitrogênio (N)
ggplot(df, aes(y = N)) +
  geom_boxplot(fill = "lightblue") +
  ggtitle("Boxplot de Nitrogênio (N)")

# Boxplot para Fósforo (P)
ggplot(df, aes(y = P)) +
  geom_boxplot(fill = "lightblue") +
  ggtitle("Boxplot de Fósforo (P)")

# Boxplot para Potássio (K)
ggplot(df, aes(y = K)) +
  geom_boxplot(fill = "lightblue") +
  ggtitle("Boxplot de Potássio (K)")

# Boxplot para Temperatura
ggplot(df, aes(y = temperature)) +
  geom_boxplot(fill = "lightblue") +
  ggtitle("Boxplot de Temperatura")

# Boxplot para Umidade
ggplot(df, aes(y = humidity)) +
  geom_boxplot(fill = "lightblue") +
  ggtitle("Boxplot de Umidade")

# Boxplot para Precipitação
ggplot(df, aes(y = rainfall)) +
  geom_boxplot(fill = "lightblue") +
  ggtitle("Boxplot de Precipitação")

# 4. Matriz de Correlação
# Filtrar apenas as colunas numéricas
df_numeric <- df %>%
  select(N, P, K, temperature, humidity, rainfall)

# Criar a matriz de correlação
cor_matrix <- cor(df_numeric)

# Plotar a matriz de correlação
corrplot(cor_matrix, method = "color", addCoef.col = "black", tl.col = "black", tl.cex = 0.8)
