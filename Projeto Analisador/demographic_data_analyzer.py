import pandas as pd

def calculate_demographic_data(print_data=True):
    # Leia o conjunto de dados
    df = pd.read_csv('adult.data.csv', header=None, names=[
        'age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 
        'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 
        'hours-per-week', 'native-country', 'salary'
    ], skiprows=1)

    # 1. Contagem de pessoas de cada raça
    race_count = df['race'].value_counts()

    # 2. Idade média dos homens
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. Porcentagem de pessoas com diploma de bacharel
    percentage_bachelors = round((df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100, 1)

    # 4. Porcentagem de pessoas com educação avançada que ganham mais de 50 mil
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[advanced_education & (df['salary'] == '>50K')].shape[0] / df[advanced_education].shape[0]) * 100, 1)

    # 5. Porcentagem de pessoas sem educação avançada que ganham mais de 50 mil
    lower_education = ~advanced_education
    lower_education_rich = round((df[lower_education & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0]) * 100, 1)

    # 6. Número mínimo de horas trabalhadas por semana
    min_work_hours = df['hours-per-week'].min()

    # 7. Porcentagem de pessoas que trabalham o número mínimo de horas por semana e ganham mais de 50 mil
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # 8. País com a maior porcentagem de pessoas que ganham mais de 50 mil
    country_salary = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_count = df['native-country'].value_counts()
    highest_earning_country_percentage = (country_salary / country_count * 100).sort_values(ascending=False)
    highest_earning_country = highest_earning_country_percentage.index[0]
    highest_earning_country_percentage = round(highest_earning_country_percentage.iloc[0], 1)

    # 9. Ocupação mais popular para aqueles que ganham mais de 50 mil na Índia
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    if print_data:
        print("Número de cada raça:\n", race_count) 
        print("Idade Média dos homens:", average_age_men)
        print(f"Porcentagem com Diplomas de Bacharel: {percentage_bachelors}%")
        print(f"Porcentagem com ensino superior que ganha mais de 50K: {higher_education_rich}%")
        print(f"Percentagem sem ensino superior que ganha menos de 50K: {lower_education_rich}%")
        print(f"Tempo minimo de trabalho: {min_work_hours} horas/semana")
        print(f"Porcentagem de ricos entre os que menos trabalham (horas): {rich_percentage}%")
        print("Pais com maior porcentual de ricos:", highest_earning_country)
        print(f"Maior porcentual de pessoas ricas no país: {highest_earning_country_percentage}%")
        print("Principais ocupacoes na India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
