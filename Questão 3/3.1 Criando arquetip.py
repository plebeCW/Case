# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:17:43 2024

@author: xPlebe
"""
'criando arquetipo'
import pandas as pd

# Load the data
data = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/emotions.csv', sep=';')

# Count occurrences of primary_emotion for each user_id
emotion_counts = data.groupby(['user_id', 'primary_emotion']).size().reset_index(name='count')

# Find the primary_emotion with the highest count for each user_id
dominant_emotions = emotion_counts.loc[emotion_counts.groupby('user_id')['count'].idxmax()]

# Select only the user_id and primary_emotion columns
result = dominant_emotions[['user_id', 'primary_emotion', 'count']]

# Save the result to a new CSV file
result.to_csv('C:/Users/xPlebe/Desktop/case - cw/arqutip.csv', index=False, sep=';')

print("File saved successfully.")
