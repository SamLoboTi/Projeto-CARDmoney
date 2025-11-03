#🔢  etl_cardmoney.py (carga SQL)

import pandas as pd
from sqlalchemy import create_engine

#1️⃣ Caminho do CSV refinado
# -----------------------------
csv_file = "produtos_refinados.csv"

# Verifica se o arquivo existe
if not os.path.exists(csv_file):
    raise FileNotFoundError(f"Arquivo '{csv_file}' não encontrado. Execute o tratamento de dados primeiro.")



# 2️⃣ Carregar CSV refinado
df = pd.read_csv("produtos_refinados.csv", encoding="utf-8-sig")


# 3️⃣ Criar conexão com SQLite
engine = create_engine('sqlite:///produtos.db')


# 4️⃣ Inserir dados na tabela SQL
# -----------------------------
# Se a tabela já existir, substitui ('replace')
df.to_sql('produtos', con=engine, if_exists='replace', index=False)
print("✅ Tabela 'produtos' criada e dados inseridos com sucesso no SQLite!")
print("💾 Arquivo produtos.db gerado na mesma pasta do projeto.")
print(f"📊 Total de registros inseridos: {len(df)}")












