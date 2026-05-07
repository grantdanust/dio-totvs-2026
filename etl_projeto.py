import pandas as pd

# 1. EXTRACT (Extração)
print("Iniciando Extração...")
df = pd.read_csv('sdw2023.csv')
user_ids = df['UserID'].tolist()
print(f"Usuários encontrados: {df['Nome'].tolist()}")

# 2. TRANSFORM (Transformação)
print("Transformando...")
def generate_ai_news(user_name):
    # Aqui simulamos uma lógica de negócio ou chamada de IA
    return f"Olá {user_name}, invista no seu futuro com a TOTVS e a DIO!"

# Criamos uma nova coluna com a mensagem transformada
df['News'] = df['Nome'].apply(generate_ai_news)

# 3. LOAD (Carga)
print("Loading...")
# Salvamos o resultado em um novo arquivo para entrega
df.to_csv('sdw2023_updated.csv', index=False)
print("Arquivo 'sdw2023_updated.csv' gerado com sucesso!")