import pandas as pd
import google.generativeai as genai
import os

# CONFIGURAÇÃO DO GEMINI
# Dica: Substitua 'SUA_CHAVE_AQUI' pela chave que você gerou
CHAVE_API = "COLOQUE SUA CHAVE" 
genai.configure(api_key=CHAVE_API)
model = genai.GenerativeModel('gemini-1.5-flash')

# 1. EXTRACT
print("Extraindo dados...")
df = pd.read_csv('sdw2023.csv')

# 2. TRANSFORM (Agora com IA Real!)
def gerar_mensagem_ia(nome):
    print(f"Gerando mensagem para: {nome}")
    prompt = f"Crie uma frase curta e motivacional de boas-vindas para o cliente {nome} que está começando a usar os sistemas da TOTVS. Seja criativo!"
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Olá {nome}, bem-vindo à evolução tecnológica!"

print("Iniciando Transformação com Gemini...")
df['News'] = df['Nome'].apply(gerar_mensagem_ia)

# 3. LOAD
print("Salvando resultados...")
df.to_csv('sdw2023_updated.csv', index=False)
print("Sucesso! Verifique o arquivo 'sdw2023_updated.csv'")
