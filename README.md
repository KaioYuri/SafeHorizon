# SafeHorizon: Earthquake Edition

## Descrição do Projeto

O projeto **SafeHorizon: Earthquake Edition** visa prever e analisar terremotos ao redor do mundo usando dados históricos coletados da USGS. O objetivo é fornecer previsões sobre a ocorrência de terremotos e visualizações interativas para ajudar na compreensão dos padrões sísmicos.

## Estrutura do Projeto

- `data/`: Dados brutos e processados.
- `src/`: Código fonte.
  - `data_collection/`: Scripts para coletar dados da API da USGS.
  - `preprocessing/`: Scripts para limpeza e preparação dos dados.
  - `modeling/`: Scripts para treinamento de modelos de previsão.
  - `visualization/`: Scripts para criação de visualizações e dashboards.
- `notebooks/`: Notebooks Jupyter para análise exploratória dos dados.
- `docs/`: Documentação do projeto.

## Como Rodar o Projeto

1. **Coletar Dados**: Execute `src/data_collection/collect_data.py` para baixar os dados.
2. **Processar Dados**: Execute `src/preprocessing/preprocess_data.py` para limpar e preparar os dados.
3. **Treinar o Modelo**: Execute `src/modeling/train_model.py` para treinar o modelo e gerar previsões.
4. **Visualizar Resultados**: Execute `src/visualization/visualize_data.py` para criar visualizações interativas.

## Dependências

- `requests`
- `pandas`
- `fbprophet`
- `plotly`

## Licença

[Detalhes sobre a licença]
