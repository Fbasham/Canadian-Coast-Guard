import pandas as pd

df1 = pd.read_csv('inv.csv',encoding='iso8859')
df2 = pd.read_csv('asset.csv')
df3 = pd.read_csv('serial.csv')

df = df1.merge(df2.drop_duplicates('asset'),on='itemnum',how='outer').merge(df3,on='asset',how='outer')
df.to_csv('res.csv',index=False,encoding='iso8859')