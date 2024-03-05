"""App file."""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Application title
st.title('Interactive Dashboard')

# Load data
data = pd.read_csv(
    'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
)

# Sidebar with filter options
st.sidebar.title('Filters')
survived = st.sidebar.selectbox('Survived:', ['All', 'Yes', 'No'])
st.sidebar.title('Others')
st.sidebar.title('Others')
st.sidebar.title('Others')
st.sidebar.title('Others')

# Apply filters
if survived == 'Yes':
    data = data[data['Survived'] == 1]
elif survived == 'No':
    data = data[data['Survived'] == 0]

# Visualizations
st.subheader('Age Distribution')
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=20, kde=True)
st.pyplot()

st.subheader('Fare Distribution')
plt.figure(figsize=(10, 6))
sns.histplot(data['Fare'], bins=20, kde=True)
st.pyplot()

st.subheader('Survivors Distribution')
survived_counts = data['Survived'].value_counts()
st.bar_chart(survived_counts)

# Data table
st.subheader('Filtered Data')
st.write(data)
