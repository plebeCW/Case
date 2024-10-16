# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:45:51 2024

@author: xPlebe
"""


import pandas as pd
import matplotlib.pyplot as plt

# Read the data from CSV files
architype_df = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/arqutip.csv', sep=';')
users_df = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/users.csv', sep=';')

# Merge the data on user_id
merged_df = pd.merge(architype_df, users_df, on='user_id', how='inner')

# Calculate the average interest rate for each primary emotion
average_interest_rate = merged_df.groupby('primary_emotion')['interest_rate'].mean().reset_index()

# Plotting
plt.figure(figsize=(8, 5))
plt.bar(average_interest_rate['primary_emotion'], average_interest_rate['interest_rate'], color='skyblue')
plt.xlabel('Primary Emotion')
plt.ylabel('Average Interest Rate')
plt.title('Average Interest Rate by Primary Emotion')
plt.xticks(rotation=45)
plt.grid(axis='y')

# Show the plot
plt.tight_layout()
plt.show()
