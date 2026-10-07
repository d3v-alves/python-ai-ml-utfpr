import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

try:
    df = pd.read_csv("raw_titles.csv")
    print("✅ Dataset carregado com sucesso!\n")
except FileNotFoundError:
    print(
        "❌ Arquivo 'raw.csv' não encontrado. Verifique se o nome ou o caminho estão corretos."
    )
    exit()

print("--- Primeiras 5 linhas do dataset ---")
print(df.head(), "\n")
print("--- Informações estruturais do dataset ---")
print(df.info(), "\n")

print("--- 2. Limpeza dos Dados ---")

nulos_por_coluna = df.isnull().sum()
print("Valores nulos por coluna:")
print(nulos_por_coluna[nulos_por_coluna > 0], "\n")

duplicados = df.duplicated().sum()
print(f"Total de linhas completamente duplicadas: {duplicados}\n")

if duplicados > 0:
    df = df.drop_duplicates()
    print("👉 Linhas duplicadas removidas.")

coluna_nota = [c for c in df.columns if "rating" in c.lower() or "score" in c.lower()][0]
df = df.dropna(subset=[coluna_nota])
print(f"👉 Linhas com valores nulos na coluna '{coluna_nota}' foram removidas.\n")

print(f"--- 3. Estatística Básica da coluna: {coluna_nota} ---")

media = df[coluna_nota].mean()
mediana = df[coluna_nota].median()
moda = df[coluna_nota].mode()[0]  # Pega a primeira moda encontrada
desvio_padrao = df[coluna_nota].std()

print(f"Média: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda:.2f}")
print(f"Desvio Padrão: {desvio_padrao:.2f}\n")

print("--- 4. Gerando Gráficos (Feche as janelas dos gráficos para o script continuar) ---")

coluna_tipo = [c for c in df.columns if "type" in c.lower() or "category" in c.lower()][0]

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x=coluna_tipo, palette="Set2")
plt.title("Distribuição de Conteúdo na Netflix (Filmes vs Séries)")
plt.xlabel("Tipo de Conteúdo")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x=coluna_nota, kde=True, color="skyblue", bins=20)
plt.axvline(media, color="red", linestyle="--", label=f"Média ({media:.2f})")
plt.axvline(mediana, color="green", linestyle="-.", label=f"Mediana ({mediana:.2f})")
plt.title(f"Distribuição das Avaliações dos Títulos ({coluna_nota})")

plt.xlabel("Nota no IMDB")
plt.ylabel("Frequência")
plt.legend()
plt.tight_layout()
plt.show()

print("🏁 Processo concluído com sucesso!")
