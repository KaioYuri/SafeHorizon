import pandas as pd
import plotly.express as px

# Carregar dados limpos e previsões
data = pd.read_csv('data/cleaned_earthquake_data.csv')
forecast = pd.read_csv('data/forecast.csv')

# Visualizar dados históricos
fig = px.scatter_geo(data,
                     lon='longitude',
                     lat='latitude',
                     color='magnitude',
                     hover_name='magnitude',
                     title='Terremotos Históricos')
fig.write_html('visualizations/historical_earthquakes.html')

# Visualizar previsões
fig = px.line(forecast, x='ds', y='yhat', title='Previsões de Magnitude de Terremotos')
fig.write_html('visualizations/forecast.html')
