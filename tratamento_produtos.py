#🧹 tratamento_produtos.py (limpeza/refino)

import pandas as pd 

#1️⃣ Carregar dados brutos - CSV inicial gerado pelo scraper ou API
df = pd.read_csv("produtos_dummy.csv", encoding="utf-8-sig")
print("🔍 Dados originais:")
print(df.info())

#2️⃣ limpeza e padronização remover espaços e colunas extras
df.columns = df.columns.str.strip() 

# Padroniza colunas de texto
df["Produto"] = df["Produto"].str.strip().str.title()  
df["Categoria"] = df["Categoria"].str.strip().str.lower()  # minúsculas
df["Descrição"] = df["Descrição"].str.strip()

#3️⃣ Adicionar coluna Estoque se existir na API forneça 'stock', usar; senão criar coluna padrão com 0
if "Estoque" not in df.columns and "stock" in df.columns:
    df["Estoque"] = df["stock"].astype(int)
elif "Estoque" not in df.columns:
    df["Estoque"] = 0 


#4️⃣ Conversão de tipos de id para inteiros e preço para valores
df["ID"] = df["ID"].astype(int)
df["Preço"] = df["Preço"].astype(float)
df["Estoque"] = df["Estoque"].astype(int)


#5️⃣ Remover duplicidades
df.drop_duplicates(subset=["ID"], inplace=True)

#6️⃣ Preencher valores nulos
df.fillna(         
 {"Produto": "Sem nome",
    "Categoria": "sem categoria",
    "Descrição": "Sem descrição",
    "Estoque": 0
}, inplace=True)


#7️⃣ Remover preços negativos (opcional, caso exista algum)
df = df[df["Preço"] >= 0]

#8️⃣ Resumo
print("✅ Dados tratados:")
print(df.info())
print(df.head())

# 9️⃣ Salvar CSV refinado
df.to_csv("produtos_refinados.csv", index=False, encoding="utf-8-sig")
print("💾 Arquivo 'produtos_refinados.csv' pronto para carga em SQL!")



