# Pipeline de ETL com Python (DIO - TOTVS)

## Objetivo
Este projeto demonstra um pipeline ETL simples que extrai nomes de usuários de um arquivo CSV, aplica uma transformação gerando uma mensagem personalizada e carrega os dados em um novo arquivo.

## Etapas
1. **Extract**: Leitura do arquivo `sdw2023.csv`.
2. **Transform**: Criação de mensagens personalizadas para cada usuário.
3. **Load**: Exportação dos dados atualizados para `sdw2023_updated.csv`.

## Como executar
- Instale o Pandas: `pip install pandas` 
- Execute o script: `python etl_projeto.py`