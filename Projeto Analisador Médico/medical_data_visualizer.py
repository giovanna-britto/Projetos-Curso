import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2).apply(lambda x: 1 if x > 25 else 0)

# 3
df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)


# 4
def draw_cat_plot():
    # 5. Transformar os dados em formato longo
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    
    # 6. Agrupar e contar os valores
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7. Desenhar o gráfico categórico
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', kind='bar', data=df_cat).fig

    # 9. Salvar o gráfico
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11. Limpar os dados filtrando os valores incorretos
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12. Calcular a matriz de correlação
    corr = df_heat.corr()

    # 13. Criar uma máscara para o triângulo superior
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Configurar a figura do `matplotlib`
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15. Desenhar o `heatmap`
    sns.heatmap(corr, annot=True, fmt='.1f', mask=mask, square=True, linewidths=.5, cbar_kws={"shrink": .45}, ax=ax)

    # 16. Salvar o gráfico
    fig.savefig('heatmap.png')
    return fig

