# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 20:52:58 2024

@author: xPlebe
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the merged dataset
merged_data_path = 'C:/Users/xPlebe/Desktop/case - cw/loan_emotions.csv'
merged_data = pd.read_csv(merged_data_path, sep=';')

# Convert date columns to datetime
merged_data['issue_date'] = pd.to_datetime(merged_data['issue_date'], format='%d/%m/%Y', errors='coerce')
# You can convert other date columns if needed
# merged_data['due_date'] = pd.to_datetime(merged_data['due_date'], format='%d/%m/%Y', errors='coerce')

# Display the first few rows of the dataset
print(merged_data.head())

# Data exploration: check the data types and missing values
print(merged_data.info())

# Encode categorical variables (like primary_emotion, relationship, etc.)
merged_data_encoded = pd.get_dummies(merged_data, columns=['primary_emotion', 'relationship', 'situation', 'location', 'weather', 'physical_state', 'preceding_event'], drop_first=True)

# Keep only numeric columns for correlation
numeric_data = merged_data_encoded.select_dtypes(include=['float64', 'int64'])

# Calculate correlation matrix
correlation_matrix = numeric_data.corr()

# Boxplot to show the distribution of loan amounts across different primary emotions
plt.figure(figsize=(12, 6))
sns.boxplot(data=merged_data, x='primary_emotion', y='loan_amount', palette='pastel')
plt.title('Loan Amount Distribution by Primary Emotion')
plt.xlabel('Primary Emotion')
plt.ylabel('Loan Amount')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
