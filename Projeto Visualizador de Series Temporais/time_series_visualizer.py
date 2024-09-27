import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# 1. Importar dados e definir o índice para a coluna `date`
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# 2. Limpar dados
df = df[
    (df['value'] >= df['value'].quantile(0.025)) & 
    (df['value'] <= df['value'].quantile(0.975))
]

def draw_line_plot():
    # 3. Desenhar o gráfico de linhas
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df.index, df['value'], color='red')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Salvar e retornar a figura
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copiar e modificar os dados para o gráfico de barras mensal
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Agrupar os dados para obter a média das visualizações por mês e ano
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Criar a ordem dos meses para o gráfico
    month_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]

    # Desenhar o gráfico de barras
    fig = df_bar.plot(kind='bar', figsize=(10, 6)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.title('Monthly Average Page Views')
    plt.legend(title='Months', labels=month_order)

    # Salvar e retornar a figura
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # 5. Preparar dados para os gráficos de caixa
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    df_box['month_num'] = df_box['date'].dt.month

    # Ordenar os meses
    df_box = df_box.sort_values('month_num')

    # Desenhar os gráficos de caixa
    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1])
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Salvar e retornar a figura
    fig.savefig('box_plot.png')
    return fig
