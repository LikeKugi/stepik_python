import pandas as pd
import csv

df = pd.ExcelFile("data.xlsx").parse() # формируем dataframe

df_sorted = df.sort_values(by=['ККал на 100', 'Unnamed: 0'], ascending=[False, True])

print(df_sorted)
df_top = df_sorted.head()
