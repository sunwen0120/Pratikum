import pandas as pd
import numpy as np

# print(pd.options.display.max_column)
df = pd.read_csv("Getranke.csv",sep=';', encoding ='utf-8')
df_Getranke = pd.DataFrame(df)

print(df_Getranke)
