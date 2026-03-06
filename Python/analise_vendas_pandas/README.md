# Análises de vendas com Pandas

## 📺 Preview
![analise_final](imagem/final.png)

## 📌 Objetivo
Fazer uma análise em um dataset (.csv), permitindo identificar faturamento total, produto com maior faturamento, vendedor com o melhor faturamento, faturamento por forma de pagamento e quantidade total de vendas por vendedor. Crie, também, um arquivo .xlsx para análise no Excel.

## 📝 Dataset
Dados fictícios de vendas contendo:
- Data
- Vendedor
- Produto
- Forma de Pagamento
- Preço Unitário
- Quantidade
- Faturamento

## 💻 Tecnologias Utilizadas
- Python
- Pandas
- Jupyter Notebook

## 🐼 Principais funções do Pandas Utilizadas
- `read_csv()`: fazendo a leitura do arquivo .csv  
- `drop()`: removendo colunas vazias
- `replace()`: substituindo strings
- `astype()`: alterando tipo de colunas
- `to_excel()`: exportando .csv para excel
- `sum()`: rotornando o somatório total de colunas númericas
- `groupby()`: realizando agrupamentos para cálculos de KPI's e Dataframes
- `sort_values()`: ordenando resultados 
- `rename()`: alterando nome de colunas

## ⚙️ Etapas da análise
1. Leitura do arquivo CSV
2. Transformando o dataset e gerando um arquivo Excel
3. Análises de KPI's
4. Gerando Dataframes

## 📈 Resultado
A análise final permite identificar:
- Faturamento total
- Produto com maior faturamento
- Vendedor com o melhor faturamento
- Faturamento por forma de pagamento
- Quantidade total de vendas por vendedor
