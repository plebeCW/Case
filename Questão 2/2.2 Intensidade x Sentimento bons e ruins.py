# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 17:52:48 2024

@author: xPlebe
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
