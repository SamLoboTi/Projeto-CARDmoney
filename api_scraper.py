#🔍  api_scraper.py (coleta)
import requests
import pandas as pd

url = "https://dummyjson.com/products"

print("🔍 Conectando à API...")


response = requests.get(url)

if response.status_code == 200:
    print("✅ Conexão bem-sucedida!")
    data = response.json()


    produtos = []

    for item in data["products"]:
        produtos.append({
            "ID": item["id"],
            "Produto": item["title"],
            "Categoria": item["category"],
            "Preço": item["price"],
            "Descrição": item["description"]
        })
    df = pd.DataFrame(produtos)
    df.to_csv("produtos_dummy.csv",index=False, encoding="utf-8-sig")  
    print("Arquivo 'produtos_dummy.csv' salvo com sucesso!")






