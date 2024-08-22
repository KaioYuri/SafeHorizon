import requests
import pandas as pd

# Parâmetros para a API da USGS
url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
params = {
    "format": "geojson",
    "starttime": "1974-01-01",
    "endtime": "2024-08-21",
    "minmagnitude": 4.0
}

# Requisição para a API
response = requests.get(url, params=params)
data = response.json()

# Transformando os dados em DataFrame
earthquakes = pd.json_normalize(data['features'])

# Salvando os dados em CSV
earthquakes.to_csv('data/earthquake_data.csv', index=False)
