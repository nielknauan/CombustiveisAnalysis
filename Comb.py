import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Leia os dados do arquivo Excel
df = pd.read_excel(r'')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Ordenar o DataFrame pelo índice de datas
df.sort_index(inplace=True)

# Delimite um intervalo de datas inferior e superior
inferior = '2010-01-01'
superior = '2020-12-31'

# Filtrar o DataFrame para incluir apenas o intervalo de datas especificado
df_filtered = df.loc[inferior:superior]

# Ajuste o modelo ARIMA
model = ARIMA(df_filtered['Price'], order=(5, 1, 0))
model_fit = model.fit()

# Configure a figura e os eixos
plt.figure(figsize=(12, 6))

# Plotar o histórico de preços
plt.plot(df_filtered['Price'], label='Histórico de Preços', color='blue')

# Adicionar linha mínima
min_value = 2200
plt.axhline(y=min_value, color='red', linestyle='--', label='Mínimo')

# Adicionar linha máxima
max_value = 3800
plt.axhline(y=max_value, color='Green', linestyle='--', label='Máximo')

# Adicionar título e legendas
plt.title('Preços dos Combustíveis ao Longo do Tempo')
plt.xlabel('Data')
plt.ylabel('Preço do Combustível')
plt.legend()
plt.grid(True)

# Mostrar o gráfico
plt.show()