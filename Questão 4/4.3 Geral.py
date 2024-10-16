# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 20:08:39 2024

@author: xPlebe
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV files
loans_df = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/loans.csv', sep=';')
users_df = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/users.csv', sep=';')

# Convert dates in loans DataFrame
loans_df['issue_date'] = pd.to_datetime(loans_df['issue_date'], format='%d/%m/%Y')
loans_df['due_date'] = pd.to_datetime(loans_df['due_date'], format='%d/%m/%Y')
loans_df['paid_date'] = pd.to_datetime(loans_df['paid_date'], errors='coerce')

# Calculate additional metrics in loans DataFrame
loans_df['interest_earned'] = loans_df['total_amount'] - loans_df['loan_amount']
loans_df['repaid'] = loans_df['status'] == 'paid'

# Extract year for grouping
loans_df['year'] = loans_df['issue_date'].dt.year

# Group by year to analyze trends
annual_data = loans_df.groupby('year').agg(
    total_disbursed=('loan_amount', 'sum'),
    total_revenue=('total_amount', 'sum'),
    total_profit=('interest_earned', 'sum'),
    total_loans=('loan_id', 'count'),
    repaid_loans=('repaid', 'sum'),
).reset_index()

# Calculate repayment rate
annual_data['repayment_rate'] = annual_data['repaid_loans'] / annual_data['total_loans'] * 100

# Plotting Total Loan Amount Disbursed Over Time
plt.figure(figsize=(12, 6))
plt.plot(annual_data['year'], annual_data['total_disbursed'], marker='o', color='blue')
plt.title('Total Loan Amount Disbursed Over Time')
plt.xlabel('Year')
plt.ylabel('Total Loan Amount Disbursed')
plt.xticks(annual_data['year'])
plt.grid()
plt.tight_layout()
plt.show()

# Plotting Loan Performance
plt.figure(figsize=(12, 6))
bar_width = 0.35
x = annual_data['year']
plt.bar(x - bar_width/2, annual_data['total_loans'], width=bar_width, label='Total Loans', color='lightblue')
plt.bar(x + bar_width/2, annual_data['repaid_loans'], width=bar_width, label='Repaid Loans', color='orange')
plt.title('Loan Performance Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Loans')
plt.xticks(annual_data['year'])
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# Plotting Total Revenue and Profit Over Time
plt.figure(figsize=(12, 6))
plt.plot(annual_data['year'], annual_data['total_revenue'], marker='o', label='Total Revenue', color='green')
plt.plot(annual_data['year'], annual_data['total_profit'], marker='o', label='Total Profit', color='purple')
plt.title('Total Revenue and Profit Over Time')
plt.xlabel('Year')
plt.ylabel('Amount')
plt.xticks(annual_data['year'])
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()
