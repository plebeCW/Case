# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 17:50:44 2024

@author: xPlebe
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the dataset
emotions = pd.read_csv('C:/Users/xPlebe/Desktop/case - cw/emotions.csv', sep=';')

# Fill missing values
emotions['location'] = emotions['location'].fillna('unknown')
emotions['primary_emotion'] = emotions['primary_emotion'].fillna('unknown')
emotions['time_of_day'] = emotions['time_of_day'].fillna('unknown')
emotions['weather'] = emotions['weather'].fillna('unknown')
emotions['physical_state'] = emotions['physical_state'].fillna('unknown')
emotions['relationship'] = emotions['relationship'].fillna('unknown')

# Streamlit dashboard setup
st.title("Emotion Analysis Dashboard")

# Selection box for the different situations
option = st.selectbox(
    'Select a factor to analyze:',
    ('Location vs Primary Emotions', 
     'Time of Day vs Primary Emotions', 
     'Weather vs Primary Emotions', 
     'Physical State vs Primary Emotions', 
     'Relationship vs Primary Emotions')
)

# Function to create heatmap
def plot_heatmap(x):
    situation_emotion_distribution = emotions.groupby([x, 'primary_emotion']).size().unstack(fill_value=0)
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(situation_emotion_distribution, cmap='coolwarm', annot=False)
    plt.title(f'{x} vs Primary Emotions')
    plt.xlabel('Primary Emotion')
    plt.ylabel(x)
    plt.xticks(rotation=90)
    
    # Display the plot in Streamlit
    st.pyplot(plt)

# Display the corresponding heatmap based on selection
if option == 'Location vs Primary Emotions':
    plot_heatmap('location')
elif option == 'Time of Day vs Primary Emotions':
    plot_heatmap('time_of_day')
elif option == 'Weather vs Primary Emotions':
    plot_heatmap('weather')
elif option == 'Physical State vs Primary Emotions':
    plot_heatmap('physical_state')
elif option == 'Relationship vs Primary Emotions':
    plot_heatmap('relationship')
