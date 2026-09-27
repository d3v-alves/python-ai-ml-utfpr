import numpy as np
from sklearn.linear_model import LinearRegression

print("🤖 Iniciando teste de Inteligência Artificial...")

# 1. Criamos dados de treino (X = Tamanho de casas em m², y = Preço em milhares de reais)
# Queremos que a IA aprenda a relação: Preço = m² * 3 + 50
X_treino = np.array([[50], [60], [70], [80], [100]])
y_treino = np.array([200, 230, 260, 290, 350])

# 2. Criamos o modelo de IA e treinamos com os dados
modelo = LinearRegression()
modelo.fit(X_treino, y_treino)
print("✅ Modelo de Machine Learning treinado com sucesso!")

# 3. Fazemos uma previsão para uma casa nova de 120m² (O esperado é dar 410)
casa_nova = np.array([[120]])
preco_previsto = modelo.predict(casa_nova)

print(f"🏠 Previsão para uma casa de 120m²: R$ {preco_previsto[0]:.2f} mil!")
