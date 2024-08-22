import pandas as pd
from fbprophet import Prophet

# Carregar os dados limpos
data = pd.read_csv('data/cleaned_earthquake_data.csv')

# Preparar os dados para o Prophet
df = data[['time', 'magnitude']]
df.columns = ['ds', 'y']

# Modelo Prophet
model = Prophet()
model.fit(df)

# Fazer previsões
future = model.make_future_dataframe(periods=1825)  # Previsão para os próximos 5 anos
forecast = model.predict(future)

# Salvar previsões
forecast.to_csv('data/forecast.csv', index=False)
