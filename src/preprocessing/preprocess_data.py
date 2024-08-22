import pandas as pd

# Carregar os dados
data = pd.read_csv('data/earthquake_data.csv')

# Limpeza de dados
# Excluir colunas irrelevantes
data = data[['properties.time', 'properties.mag', 'geometry.coordinates']]
data.columns = ['time', 'magnitude', 'coordinates']

# Converter o timestamp para datetime
data['time'] = pd.to_datetime(data['time'], unit='ms')

# Separar coordenadas
data[['longitude', 'latitude', 'depth']] = pd.DataFrame(data['coordinates'].tolist(), index=data.index)
data.drop(columns='coordinates', inplace=True)

# Salvar dados limpos
data.to_csv('data/cleaned_earthquake_data.csv', index=False)
