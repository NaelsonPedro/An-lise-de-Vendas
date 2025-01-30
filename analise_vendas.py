import pandas as pd
import matplotlib.pyplot as plt

# Criando um DataFrame com dados fictícios de vendas
def criar_dataframe():
    dados = {
        'Produto': ['Fones de ouvido', 'Carregadores', 'Celular', 'Capas', 'Películas'],
        'Vendas': [15, 20, 30, 10, 25],
        'Desconto': [10, 15, 20, 5, 10],
        'Custo': [10, 15, 20, 5, 10]
    }
    return pd.DataFrame(dados)


def calcular_estatisticas(df):
    total_vendas = df['Vendas'].sum()
    media_descontos = df['Desconto'].mean()
    df['Lucro'] = df['Vendas'] - df['Custo']
    return total_vendas, media_descontos


def plotar_graficos(df):
    plt.bar(df['Produto'], df['Vendas'])
    plt.xlabel('Produto')
    plt.ylabel('Vendas')
    plt.title('Vendas por Produto')
    plt.show()


def main():
    df = criar_dataframe()
    print(df)
    total_vendas, media_descontos = calcular_estatisticas(df)
    print(f'Total de Vendas: {total_vendas}')
    print(f'Média de Descontos: {media_descontos}')
    print(df)
    plotar_graficos(df)


if __name__ == "__main__":
    main()

