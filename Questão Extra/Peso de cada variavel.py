# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:03:14 2024

@author: xPlebe
"""


'QUESTÃO NÚMERO 2'
#Peso das váriaveis.
'Apenas emoções primárias e intensidade afetam, como demonstra os gráficos a seguir.'

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

# Carregar o dataset
emotions = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/emotions.csv', sep=';')

# 1. Análise descritiva por coluna categórica
categorical_columns = ['time_of_day', 'primary_emotion', 'relationship', 'situation', 'location', 'weather', 'physical_state', 'preceding_event']

for col in categorical_columns:
    print(f'\nEstatísticas descritivas para {col}:')
    print(emotions.groupby(col)['grade'].describe())

# 2. Correlação para a coluna numérica
correlation = emotions[['intensity', 'grade']].corr()
print('\nCorrelação entre intensidade e nota do sentimento:')
print(correlation)

# 3. Visualizações Gráficas

# Boxplot para time_of_day
plt.figure(figsize=(12, 8))
sns.boxplot(x='time_of_day', y='grade', data=emotions)
plt.title('Boxplot: Hora do Dia vs Nota')
plt.xlabel('Hora do Dia')
plt.ylabel('Nota')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Boxplot para primary_emotion
plt.figure(figsize=(12, 8))
sns.boxplot(x='primary_emotion', y='grade', data=emotions)
plt.title('Boxplot: Emoção Primária vs Nota')
plt.xlabel('Emoção Primária')
plt.ylabel('Nota')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Boxplot para relationship
plt.figure(figsize=(12, 8))
sns.boxplot(x='relationship', y='grade', data=emotions)
plt.title('Boxplot: Relacionamento vs Nota')
plt.xlabel('Relacionamento')
plt.ylabel('Nota')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Boxplot para situation
plt.figure(figsize=(12, 8))
sns.boxplot(x='situation', y='grade', data=emotions)
plt.title('Boxplot: Situação vs Nota')
plt.xlabel('Situação')
plt.ylabel('Nota')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Boxplot para location
plt.figure(figsize=(12, 8))
sns.boxplot(x='location', y='grade', data=emotions)
plt.title('Boxplot: Localização vs Nota')
plt.xlabel('Localização')
plt.ylabel('Nota')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Boxplot para weather
plt.figure(figsize=(12, 8))
sns.boxplot(x='weather', y='grade', data=emotions)
plt.title('Boxplot: Clima vs Nota')
plt.xlabel('Clima')
plt.ylabel('Nota')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Boxplot para physical_state
plt.figure(figsize=(12, 8))
sns.boxplot(x='physical_state', y='grade', data=emotions)
plt.title('Boxplot: Estado Físico vs Nota')
plt.xlabel('Estado Físico')
plt.ylabel('Nota')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Boxplot para preceding_event
plt.figure(figsize=(12, 8))
sns.boxplot(x='preceding_event', y='grade', data=emotions)
plt.title('Boxplot: Evento Precedente vs Nota')
plt.xlabel('Evento Precedente')
plt.ylabel('Nota')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Scatter Plot para Intensidade vs Nota do Sentimento
plt.figure(figsize=(12, 8))
sns.scatterplot(x='intensity', y='grade', data=emotions)
plt.title('Scatter Plot: Intensidade vs Nota do Sentimento')
plt.xlabel('Intensidade')
plt.ylabel('Nota do Sentimento')
plt.tight_layout()
plt.show()

# 4. Análise de Regressão
# Converter variáveis categóricas em dummies
emotions_dummies = pd.get_dummies(emotions, drop_first=True)

# Definir variável dependente e independentes
X = emotions_dummies.drop('grade', axis=1)
y = emotions_dummies['grade']

# Adicionar uma constante para o modelo
X = sm.add_constant(X)

# Ajustar o modelo
model = sm.OLS(y, X).fit()

# Resumo do modelo
print(model.summary())


# Carregar o dataset
emotions = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/emotions.csv', sep=';')

# Definir emoções boas e ruins
good_emotions = ['joy', 'relief', 'trust', 'anticipation', 'pride']
bad_emotions = ['sadness', 'shame', 'boredom', 'anger']

# Criar uma nova coluna categórica para sentimentos bons e ruins
def categorize_emotion(emotion):
    if emotion in good_emotions:
        return 'Good Emotion'
    elif emotion in bad_emotions:
        return 'Bad Emotion'
    else:
        return 'Neutral'

emotions['emotion_category'] = emotions['primary_emotion'].apply(categorize_emotion)

# Filtrar apenas as emoções boas e ruins
filtered_emotions = emotions[emotions['emotion_category'].isin(['Good Emotion', 'Bad Emotion'])]

# Configurar o estilo do seaborn
sns.set(style='whitegrid')

# Criar um gráfico de dispersão
plt.figure(figsize=(12, 8))
sns.scatterplot(x='intensity', y='grade', hue='emotion_category', style='emotion_category', data=filtered_emotions, s=100)
plt.title('Comparação entre Emoção (Bons vs Ruins), Intensidade e Nota')
plt.xlabel('Intensidade')
plt.ylabel('Nota do Sentimento')
plt.legend(title='Categoria de Emoção', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# Análise descritiva para emoções boas e ruins
print(filtered_emotions.groupby('emotion_category')[['intensity', 'grade']].describe())

# Load the dataset
emotions = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/emotions.csv', sep=';')

# Fill missing values in relevant columns
emotions['situation'].fillna('unknown', inplace=True)
emotions['primary_emotion'].fillna('unknown', inplace=True)

# Ensure the 'grade' column has no missing values before calculating the mean
emotions['grade'].fillna(0, inplace=True)

# List of variables to analyze with primary_emotion
variaveis_para_analisar = [
    'time_of_day', 'relationship', 'situation', 'location',
    'weather', 'physical_state', 'preceding_event'
]

# Select a variable for analysis
for i in range(6):
    variavel_selecionada = variaveis_para_analisar[i]  # Choose the variable
    
    # Group data and calculate the mean of the 'grade' column
    situation_emotion_distribution = emotions.groupby([variavel_selecionada, 'primary_emotion'])['grade'].mean().unstack()
    
    # Create the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(situation_emotion_distribution, cmap='coolwarm', annot=True, fmt='.2f')
    plt.title(f'Mean Grade for {variavel_selecionada.capitalize()} vs Primary Emotions')
    plt.xlabel('Primary Emotion')
    plt.ylabel(variavel_selecionada.capitalize())
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Show the heatmap
    plt.show()

# Load the dataset
emotions = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/emotions.csv', sep=';')

# Fill missing values in relevant columns
emotions['situation'].fillna('unknown', inplace=True)
emotions['primary_emotion'].fillna('unknown', inplace=True)

# Ensure the 'intensity' column has no missing values before calculating the mean
emotions['intensity'].fillna(0, inplace=True)

# List of variables to analyze with primary_emotion
variaveis_para_analisar = [
    'time_of_day', 'relationship', 'situation', 'location',
    'weather', 'physical_state', 'preceding_event'
]

# Select a variable for analysis
for i in range(6):
    variavel_selecionada = variaveis_para_analisar[i]  # Choose the variable
    
    # Group data and calculate the mean of the 'intensity' column
    situation_emotion_distribution = emotions.groupby([variavel_selecionada, 'primary_emotion'])['intensity'].mean().unstack()
    
    # Create the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(situation_emotion_distribution, cmap='coolwarm', annot=True, fmt='.2f')
    plt.title(f'Mean Intensity for {variavel_selecionada.capitalize()} vs Primary Emotions')
    plt.xlabel('Primary Emotion')
    plt.ylabel(variavel_selecionada.capitalize())
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Show the heatmap
    plt.show()
    
    
# Load the dataset
emotions = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/emotions.csv', sep=';')

# Fill missing values in relevant columns
emotions['situation'].fillna('unknown', inplace=True)
emotions['primary_emotion'].fillna('unknown', inplace=True)

# Ensure the 'grade' column has no missing values before calculating the mean
emotions['grade'].fillna(0, inplace=True)

# List of variables to analyze with primary_emotion
variaveis_para_analisar = [
    'time_of_day', 'relationship', 'situation', 'location',
    'weather', 'physical_state', 'preceding_event'
]

# Select a variable for analysis
for i in range(6):
    variavel_selecionada = variaveis_para_analisar[i]  # Choose the variable
    
    # Group data and calculate the mean of the 'grade' column
    situation_emotion_distribution = emotions.groupby([variavel_selecionada, 'primary_emotion'])['grade'].mean().unstack()
    
    # Create the heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(situation_emotion_distribution, cmap='coolwarm', annot=True, fmt='.2f')
    plt.title(f'Mean Grade for {variavel_selecionada.capitalize()} vs Primary Emotions')
    plt.xlabel('Primary Emotion')
    plt.ylabel(variavel_selecionada.capitalize())
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Show the heatmap
    plt.show()