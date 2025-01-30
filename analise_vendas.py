import pandas as pd
import matplotlib.pyplot as plt

# Criando um DataFrame com dados fictícios de vendas
dados = {
    'Produto': ['Fones de ouvido', 'Carregadores', 'Celular', 'Capas', 'Películas'],
    'Vendas': [15, 20, 30, 10, 25],
    'Desconto': [10, 15, 20, 5, 10],
    'Custo': [10, 15, 20, 5, 10]
}

df = pd.DataFrame(dados)
print(df)

# Calculando o total de vendas
total_vendas = df['Vendas'].sum()
print(f'Total de Vendas: {total_vendas}')

# Calculando a média de descontos
media_descontos = df['Desconto'].mean()
print(f'Média de Descontos: {media_descontos}')

# Calculando o lucro para cada produto
df['Lucro'] = df['Vendas'] - df['Custo']
print(df)

# Criando um gráfico de barras para visualizar as vendas
plt.bar(df['Produto'], df['Vendas']) # plt.bar(): Cria um gráfico de barras.
plt.xlabel('Produto')
plt.ylabel('Vendas')
plt.title('Vendas por Produto')
plt.show()  # plt.show(): Exibe o gráfico.

# Criando um gráfico de barras para visualizar o lucro
plt.bar(df['Produto'], df['Lucro'], color = 'green')
plt.xlabel('Produto')
plt.ylabel('Lucro')
plt.title('Lucro por Produto')
plt.savefig('c:/Users/Naels/Envs/lucro_por_produto.png') # Salvando o gráfico como uma imagem
plt.show()

