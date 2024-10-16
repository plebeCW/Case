# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 18:08:22 2024

@author: xPlebe
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
