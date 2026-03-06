# %%

import pandas as pd

## fazendo a leitura do arquivo CSV 
def carregando_csv():
    dataFrame = pd.read_csv("base_vendas.csv", index_col=0)
    return dataFrame
    #print(dataFrame)

## ------------------------------------- Preparando o Data Frame ------------------------------------- ##
def preparando_csv(df):
    ## excluindo as 2 últimas colunas (colunas vazias)

    df = df.drop(["Unnamed: 7", "Unnamed: 8"], axis="columns")
    #print(type(df))

    ## Títulos das colunas: substituindo os espaços em branco por underline
    substituir_espaço = df.columns.str.replace(" ", "_")

    ## Atribuindo os títulos atualizados ao data frame
    df.columns = substituir_espaço
    #print(df)

    ## Checando os tipos das colunas do data frame
    #print(df.dtypes)

    """ Ao checar o tipo das colunas do data frame foi observado que:
    'Preço_Unitário':  está formatada como string; será necessário remover 'R$ '
    primeiro e depois formatar a coluna como float.
    """

    ## Removendo o cifrão (R$ ) da coluna Preço_Unitário e alterando o tipo da coluna
    removendo_real = df["Preço_Unitário"].str.replace("R$ ", "")
    df["Preço_Unitário"] = removendo_real
    
    ## Alterando o tipo da coluna "Preço_Unitário" para float
    df["Preço_Unitário"] = df["Preço_Unitário"].astype("float64")
    
    ## Criando a coluna 'Faturamento' (Qtd * Preço_Unitário)
    df["Faturamento"] = df["Preço_Unitário"] * df["Qtd"]
    
    ## Agora que o Data Frame está pronto será gerado um arquivo .xlsx para possível análise futura no Excel
    df.to_excel("base_de_vendas.xlsx", sheet_name="Base_Vendas")

    return df
# %%
## ------------------------------------- Análises Gerais (KPI's) ------------------------------------- ##
def indicadores_kpi(df):
    faturamento_total = df["Faturamento"].sum()
    print(f"Faturamento Total: R${faturamento_total:,.2f}")
    
    ## Buscando pelo produto que teve maior faturamento
    resultado = df.groupby("Produto")["Faturamento"].agg([sum])
    resultado = resultado.reset_index().sort_values(by="sum", ascending=False)
   
    print(f"Produto com maior faturamento: {resultado.loc[resultado['sum'].idxmax(), "Produto"]} -> R${resultado.loc[resultado['sum'].idxmax(), "sum"]:,.2f}")
    
    ## Buscando pelo vendedor que teve maior faturamento
    resultado = df.groupby("Vendedor")["Faturamento"].agg([sum])
    resultado = resultado.reset_index().sort_values(by="sum", ascending=False)
    
    print(f"Vendedor com melhor faturamento: {resultado.loc[resultado['sum'].idxmax(), "Vendedor"]} -> R${resultado.loc[resultado['sum'].idxmax(), "sum"]:,.2f}")
# %%
## ------------------------------------- DataFrame/Series ------------------------------------- ##
def dataframes_gerais(df):
    #retornando o faturamento por forma de pagamento
    f_pagamento = df.groupby("Forma_Pagamento")["Faturamento"].agg([sum])
    f_pagamento = f_pagamento.reset_index().sort_values(by="sum", ascending=False)
    f_pagamento = f_pagamento.rename(columns={"sum":"Faturamento"})
    f_pagamento["Faturamento"] = f_pagamento["Faturamento"].apply(lambda x: f"R$ {x:,.2f}")
    print("\n", f_pagamento,"\n")

    #retornando a quantidade total de vendas por vendedor
    qtd_vendas_vendedor = df.groupby("Vendedor")["Vendedor"].agg([len])
    qtd_vendas_vendedor = qtd_vendas_vendedor.reset_index().sort_values(by="len", ascending=False)
    qtd_vendas_vendedor = qtd_vendas_vendedor.rename(columns={"len":"Qtd Vendas"})
    print("\n",qtd_vendas_vendedor,"\n")
    
# %%
## ------------------------------------- Executando o Programa ------------------------------------- ##
if __name__ == "__main__":
    df = carregando_csv()
    df = preparando_csv(df)
    indicadores_kpi(df)
    dataframes_gerais(df)