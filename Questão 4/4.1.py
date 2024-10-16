# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 23:29:01 2024

@author: xPlebe
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the datasets from CSV files
user_status = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/user_status.csv', sep=';')
users = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/users.csv', sep=';')

# Merge the DataFrames based on user_id
merged_df = pd.merge(users, user_status, on='user_id')

# Create a column to indicate if the user is a debtor
merged_df['is_debtor'] = merged_df['user_status'].apply(lambda x: 1 if x == 'delinquent' else 0)

# Calculate the averages of credit_limit and interest_rate
averages = merged_df.groupby('is_debtor').agg({
    'credit_limit': 'mean',
    'interest_rate': 'mean'
}).rename(index={0: 'paying', 1: 'debtor'})

# Print the averages
print(averages)

# Create separate plots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Credit Limit Plot
averages['credit_limit'].plot(kind='bar', color='skyblue', ax=ax1)
ax1.set_title('Average Credit Limit by User Status')
ax1.set_ylabel('Average Credit Limit')
ax1.set_xticklabels(averages.index, rotation=0)

# Interest Rate Plot
averages['interest_rate'].plot(kind='bar', color='salmon', ax=ax2)
ax2.set_title('Average Interest Rate by User Status')
ax2.set_ylabel('Average Interest Rate')
ax2.set_xticklabels(averages.index, rotation=0)

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
