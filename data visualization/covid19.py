import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
file_path = r'C:\Users\DELL\Desktop\projectpy\complete.csv'
data = pd.read_csv(file_path)

# Convert 'Date' column to datetime format for time-series analysis
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Print the first few rows of the dataset
print("Dataset Overview:")
print(data.head(), '\n')

# Print summary statistics
print("Summary Statistics:")
print(data.describe(), '\n')

# Print the unique states/UTs
print("Unique States/UTs:")
print(data['Name of State / UT'].unique(), '\n')

# Visualization 1: Time Series Plot - New Cases over Time
plt.figure(figsize=(14, 6))
sns.lineplot(x='Date', y='New cases', data=data, hue='Name of State / UT', legend=False)
plt.title('Time Series of New COVID-19 Cases')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.show()

# Print total new cases over time
total_new_cases = data.groupby('Date')['New cases'].sum()
print("Total New Cases Over Time:")
print(total_new_cases, '\n')

# Visualization 2: Bar Plot - Total Confirmed Cases per State
plt.figure(figsize=(12, 8))
statewise_cases = data.groupby('Name of State / UT')['Total Confirmed cases'].max().sort_values(ascending=False)
sns.barplot(y=statewise_cases.index, x=statewise_cases.values, palette='viridis')
plt.title('Total Confirmed Cases per State/UT')
plt.xlabel('Total Confirmed Cases')
plt.ylabel('State/UT')
plt.show()

# Print total confirmed cases per state
print("Total Confirmed Cases per State/UT:")
print(statewise_cases, '\n')

# Visualization 3: Heatmap - Correlation among numerical variables
plt.figure(figsize=(10, 6))
correlation_matrix = data[['Total Confirmed cases', 'Cured/Discharged/Migrated', 'New cases', 'New deaths', 'New recovered']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Relationship Among COVID-19 Case Statistics')
plt.show()

# Print correlation coefficients
print("Relationship Among COVID-19 Case Statistics:")
print(correlation_matrix, '\n')

# Visualization 4: Scatter Plot (Geographical) - Total Confirmed Cases by Location
fig = px.scatter_geo(data, lat='Latitude', lon='Longitude', color='Total Confirmed cases', size='Total Confirmed cases',
                     hover_name='Name of State / UT', hover_data={'Latitude': False, 'Longitude': False},
                     title="Geographical Distribution of Total COVID-19 Cases")
fig.show()

# Print summary of geographical data
print("Geographical Data Overview:")
print(data[['Name of State / UT', 'Latitude', 'Longitude', 'Total Confirmed cases']].head(), '\n')

