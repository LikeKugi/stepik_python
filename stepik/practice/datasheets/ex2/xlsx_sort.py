import pandas as pd

df = pd.ExcelFile("data.xlsx").parse() # формируем dataframe

df_sorted = df.sort_values(by=['ККал на 100', 'Unnamed: 0'], ascending=[False, True])

print(*df_sorted['Unnamed: 0'].to_list(), sep='\n')
