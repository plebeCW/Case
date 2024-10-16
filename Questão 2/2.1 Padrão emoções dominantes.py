# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 21:22:04 2024

@author: xPlebe
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from a CSV file
file_path = 'C:/Users/xPlebe/Desktop/case - cw/emotions.csv'  # Update with your file path
df = pd.read_csv(file_path, sep=';')

# Convert 'timestamp' to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d/%m/%Y %H:%M')

# Extract month and year for grouping
df['month_year'] = df['timestamp'].dt.to_period('M')

# Get the top 5 primary emotions based on frequency
top_emotions = df['primary_emotion'].value_counts().nlargest(5).index.tolist()

# Filter the dataframe for only the top 5 emotions
filtered_df = df[df['primary_emotion'].isin(top_emotions)]

# Group by month/year and primary emotion
monthly_emotions = filtered_df.groupby(['month_year', 'primary_emotion']).size().unstack(fill_value=0)

# Plotting
plt.figure(figsize=(14, 7))

# Line plot for monthly emotional trends of top 5 emotions
monthly_emotions.plot(kind='line', marker='o', linewidth=2)
plt.title('Monthly Emotional Trends (Top 5 Emotions)', fontsize=16)
plt.xlabel('Month and Year', fontsize=14)
plt.ylabel('Count', fontsize=14)
plt.xticks(rotation=45)
plt.grid(True)
plt.legend(title='Primary Emotion', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

plt.show()
