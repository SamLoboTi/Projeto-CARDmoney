#🗒️ README.md detalhado

# Tratamento de Dados de Produtos - Projeto CARDmoney

## Site utilizado
- API Dummy: [https://dummyjson.com/products](https://dummyjson.com/products)
- A API fornece produtos fictícios com informações como título, categoria, preço, descrição, estoque, etc.

## Objetivo
- Limpar, padronizar e preparar os dados coletados para inserção em banco de dados SQL (SQLite, MySQL ou PostgreSQL).

## Principais etapas do processo
1. **Coleta de dados**: leitura do CSV bruto `produtos_dummy.csv` gerado pelo scraper ou API.  
2. **Limpeza e padronização**: remover espaços extras, padronizar nomes, converter categorias para minúsculas.  
3. **Adicionar coluna Estoque**: garantir que todos os produtos tenham quantidade disponível.  
4. **Conversão de tipos**: garantir tipos corretos (`int` para ID e Estoque, `float` para Preço, `str` para textos).  
5. **Remoção de duplicidades**: eliminar registros repetidos baseado no `ID`.  
6. **Tratamento de valores nulos**: preencher campos ausentes com valores padrão.  
7. **Remoção de preços inválidos**: remover produtos com preço negativo (opcional).  
8. **Salvar arquivo refinado**: gerar `produtos_refinados.csv` pronto para inserção em banco SQL.

## Exemplo de registros coletados
| ID | Produto        | Categoria  | Descrição                        | Preço | Estoque |
|----|----------------|-----------|---------------------------------|-------|--------|
| 1  | iPhone 9       | smartphone| Apple iPhone 9, 64GB, branco    | 549   | 94     |
| 2  | Samsung Galaxy | smartphone| Samsung Galaxy, 128GB, preto    | 699   | 36     |
| 3  | MacBook Pro    | laptop    | Apple MacBook Pro 16", cinza    | 1749  | 22     |

## Resultado final
- Arquivo CSV `produtos_refinados.csv` pronto para ETL.  

- Dados prontos para serem carregados em qualquer banco SQL.


[(imagem alt)https://github.com/SamLoboTi/Projeto-CARDmoney/blob/bef9d68441adbad5de76e72c93f04051743ba94a/Captura%20de%20tela_10-11-2025_13529_dbc-df17ceda-4606.cloud.databricks.com.pdf]



https://github.com/SamLoboTi/Projeto-CARDmoney/blob/bef9d68441adbad5de76e72c93f04051743ba94a/Captura%20de%20tela_10-11-2025_13529_dbc-df17ceda-4606.cloud.databricks.com.pdf




