import pandas as pd
import numpy as pd

df1 = pd.read_csv('CalibOutputs_list.csv')
df2 = pd.read_csv('BM_list.csv')

results = df2.merge(df1, on = "ID", how='inner')

results.to_csv('combined.csv', sep='\t', index=False)
