import pandas as pd

# 1 - importando os dados
data = pd.read_excel('VendaCarros.xlsx') # <- tabela original para criar a tabela pivô

# 2 - Selecionando colunas especificas no dataframe
df = data[['Fabricante', 'ValorVenda', 'Ano']]
print(df)

# 3-Criando a tabela pivô
pivot_table = df.pivot_table(
    index = 'Ano',
    columns = 'Fabricante',
    values = 'ValorVenda',
    aggfunc = 'sum'
)

print(pivot_table)

# 4 - Exportando tabela pivô em arquivo excel
pivot_table.to_excel('pivot_table.xlsx', 'Relatorio') #<- salvando a tabela