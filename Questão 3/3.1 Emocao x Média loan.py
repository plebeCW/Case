# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:44:08 2024

@author: xPlebe
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the archetype data
archetypes = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/arqutip.csv', sep=';')

# Load the loans data
loans = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/loans.csv', sep=';')

# Ensure loan_amount is treated as a string and then convert to numeric
loans['loan_amount'] = pd.to_numeric(loans['loan_amount'].astype(str).str.replace(' ', ''), errors='coerce')

# Merge the datasets on user_id
merged_data = pd.merge(archetypes, loans, on='user_id', how='inner')

# Calculate the average loan amount per primary emotion
average_borrowing = merged_data.groupby('primary_emotion')['loan_amount'].mean().reset_index()

# Rename columns for clarity
average_borrowing.columns = ['primary_emotion', 'average_loan_amount']

# Print the average borrowing results
print(average_borrowing)

# Plot the graph
plt.figure(figsize=(10, 6))
sns.barplot(x='average_loan_amount', y='primary_emotion', data=average_borrowing, palette='coolwarm')
plt.title('Average Borrowing by Primary Emotion')
plt.xlabel('Average Loan Amount')
plt.ylabel('Primary Emotion')
plt.grid(axis='x')
plt.show()
