# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:05:41 2024

@author: xPlebe
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
emotions = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/emotions.csv', sep=';')

# Fill missing values in 'situation' and 'primary_emotion' to avoid errors
emotions['location'].fillna('unknown', inplace=True)
emotions['primary_emotion'].fillna('unknown', inplace=True)

# 1. Grouping by situation and primary emotion to calculate frequencies
situation_emotion_distribution = emotions.groupby(['location', 'primary_emotion']).size().unstack(fill_value=0)

# 2. Heatmap: Visualizing how situations affect primary emotions
plt.figure(figsize=(12, 8))
sns.heatmap(situation_emotion_distribution, cmap='coolwarm', annot=False)
plt.title('Locations vs Primary Emotions')
plt.xlabel('Primary Emotion')
plt.ylabel('Location')
plt.xticks(rotation=90)
plt.show()

# Fill missing values in 'situation' and 'primary_emotion' to avoid errors
emotions['time_of_day'].fillna('unknown', inplace=True)
emotions['primary_emotion'].fillna('unknown', inplace=True)

# 1. Grouping by situation and primary emotion to calculate frequencies
situation_emotion_distribution = emotions.groupby(['time_of_day', 'primary_emotion']).size().unstack(fill_value=0)

# 2. Heatmap: Visualizing how situations affect primary emotions
plt.figure(figsize=(12, 8))
sns.heatmap(situation_emotion_distribution, cmap='coolwarm', annot=False)
plt.title('time_of_day vs Primary Emotions')
plt.xlabel('Primary Emotion')
plt.ylabel('time_of_day')
plt.xticks(rotation=90)
plt.show()

# Fill missing values in 'situation' and 'primary_emotion' to avoid errors
emotions['relationship'].fillna('unknown', inplace=True)
emotions['primary_emotion'].fillna('unknown', inplace=True)

# 1. Grouping by situation and primary emotion to calculate frequencies
situation_emotion_distribution = emotions.groupby(['relationship', 'primary_emotion']).size().unstack(fill_value=0)

# 2. Heatmap: Visualizing how situations affect primary emotions
plt.figure(figsize=(12, 8))
sns.heatmap(situation_emotion_distribution, cmap='coolwarm', annot=False)
plt.title('relationship vs Primary Emotions')
plt.xlabel('Primary Emotion')
plt.ylabel('relationship')
plt.xticks(rotation=90)
plt.show()

# Fill missing values in 'situation' and 'primary_emotion' to avoid errors
emotions['situation'].fillna('unknown', inplace=True)
emotions['primary_emotion'].fillna('unknown', inplace=True)

# 1. Grouping by situation and primary emotion to calculate frequencies
situation_emotion_distribution = emotions.groupby(['situation', 'primary_emotion']).size().unstack(fill_value=0)

# 2. Heatmap: Visualizing how situations affect primary emotions
plt.figure(figsize=(12, 8))
sns.heatmap(situation_emotion_distribution, cmap='coolwarm', annot=False)
plt.title('situation vs Primary Emotions')
plt.xlabel('Primary Emotion')
plt.ylabel('situation')
plt.xticks(rotation=90)
plt.show()

# Fill missing values in 'situation' and 'primary_emotion' to avoid errors
emotions['location'].fillna('unknown', inplace=True)
emotions['primary_emotion'].fillna('unknown', inplace=True)

# 1. Grouping by situation and primary emotion to calculate frequencies
situation_emotion_distribution = emotions.groupby(['location', 'primary_emotion']).size().unstack(fill_value=0)

# 2. Heatmap: Visualizing how situations affect primary emotions
plt.figure(figsize=(12, 8))
sns.heatmap(situation_emotion_distribution, cmap='coolwarm', annot=False)
plt.title('location vs Primary Emotions')
plt.xlabel('Primary Emotion')
plt.ylabel('location')
plt.xticks(rotation=90)
plt.show()

# Fill missing values in 'situation' and 'primary_emotion' to avoid errors
emotions['weather'].fillna('unknown', inplace=True)
emotions['primary_emotion'].fillna('unknown', inplace=True)

# 1. Grouping by situation and primary emotion to calculate frequencies
situation_emotion_distribution = emotions.groupby(['weather', 'primary_emotion']).size().unstack(fill_value=0)

# 2. Heatmap: Visualizing how situations affect primary emotions
plt.figure(figsize=(12, 8))
sns.heatmap(situation_emotion_distribution, cmap='coolwarm', annot=False)
plt.title('weather vs Primary Emotions')
plt.xlabel('Primary Emotion')
plt.ylabel('weather')
plt.xticks(rotation=90)
plt.show()

# Fill missing values in 'situation' and 'primary_emotion' to avoid errors
emotions['physical_state'].fillna('unknown', inplace=True)
emotions['primary_emotion'].fillna('unknown', inplace=True)

# 1. Grouping by situation and primary emotion to calculate frequencies
situation_emotion_distribution = emotions.groupby(['physical_state', 'primary_emotion']).size().unstack(fill_value=0)

# 2. Heatmap: Visualizing how situations affect primary emotions
plt.figure(figsize=(12, 8))
sns.heatmap(situation_emotion_distribution, cmap='coolwarm', annot=False)
plt.title('physical_state vs Primary Emotions')
plt.xlabel('Primary Emotion')
plt.ylabel('physical_state')
plt.xticks(rotation=90)
plt.show()

# Fill missing values in 'situation' and 'primary_emotion' to avoid errors
emotions['preceding_event'].fillna('unknown', inplace=True)
emotions['primary_emotion'].fillna('unknown', inplace=True)

# 1. Grouping by situation and primary emotion to calculate frequencies
situation_emotion_distribution = emotions.groupby(['preceding_event', 'primary_emotion']).size().unstack(fill_value=0)

# 2. Heatmap: Visualizing how situations affect primary emotions
plt.figure(figsize=(12, 8))
sns.heatmap(situation_emotion_distribution, cmap='coolwarm', annot=False)
plt.title('preceding_event vs Primary Emotions')
plt.xlabel('Primary Emotion')
plt.ylabel('preceding_event')
plt.xticks(rotation=90)
plt.show()