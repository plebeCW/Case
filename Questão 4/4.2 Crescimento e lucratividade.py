# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 19:40:05 2024

@author: xPlebe
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the data from CSV files
users_df = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/users.csv', sep=';')
loans_df = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/loans.csv', sep=';')

# Convert the 'issue_date' column to datetime format in the loans DataFrame
loans_df['issue_date'] = pd.to_datetime(loans_df['issue_date'], format='%d/%m/%Y')

# Extract year from the 'issue_date'
loans_df['year'] = loans_df['issue_date'].dt.year

# Merge loans with users to get interest rate for each loan
merged_df = loans_df.merge(users_df[['user_id', 'interest_rate']], on='user_id')

# Calculate total interest earned for each loan
merged_df['interest_earned'] = merged_df['total_amount'] - merged_df['loan_amount']

# Group by year and calculate metrics
annual_data = merged_df.groupby('year').agg(
    total_loans=('loan_id', 'count'),
    total_borrowed=('loan_amount', 'sum'),
    total_invoiced=('total_amount', 'sum'),
    total_interest=('interest_earned', 'sum')
).reset_index()

# Calculate profit after grouping
annual_data['profit'] = annual_data['total_invoiced'] - annual_data['total_borrowed']

# Print the annual data table
print("Annual Financial Metrics:")
print(annual_data)

# Plotting Total Loans
plt.figure(figsize=(12, 6))
plt.plot(annual_data['year'], annual_data['total_loans'], label='Total Loans', marker='o', color='blue')
plt.title('Total Loans Issued by Year')
plt.xlabel('Year')
plt.ylabel('Number of Loans')
plt.xticks(annual_data['year'])
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Plotting Other Metrics
plt.figure(figsize=(12, 6))
plt.plot(annual_data['year'], annual_data['total_borrowed'], label='Total Borrowed', marker='o', color='orange')
plt.plot(annual_data['year'], annual_data['total_invoiced'], label='Total Invoiced', marker='o', color='green')
plt.plot(annual_data['year'], annual_data['profit'], label='Profit', marker='o', color='purple')

# Adding labels and title for the second chart
plt.title('Annual Financial Metrics')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.xticks(annual_data['year'])
plt.legend()
plt.grid()
plt.tight_layout()

# Show the second plot
plt.show()

