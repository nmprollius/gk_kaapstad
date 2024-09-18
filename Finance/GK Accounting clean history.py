

import os
import pandas as pd
import numpy as np

df=pd.read_excel('Kerk income statement 2023_11.xlsx', sheet_name=None)

def clean_df(df1,year):

  finyear = year
  print(year)
  if year == 'Begroting 24':
    year='2024'
    bd = True
  else:
    bd=False
  # year = 'Begroting 24'
  # df1=df[year]
  clms = df1.iloc[1,:].to_list()
  clms[0]='code'
  clms[1]='description'
  df1=df1.iloc[2:].copy()
  df1.columns=clms
  df1.drop(columns=['Total'],inplace=True)
  df1=df1.melt(id_vars=['code','description'], var_name='month',value_name='value')
  df1['year'] = year

  # df1['year'] = df1['year'].map({'Begroting 24':2024})
  df1['year'] = np.where(df1['month'].isin(['January','February']),
                       df1['year'].astype('int'),df1['year'].astype('int')-1)
  df1['year'].unique()
  
  if bd:
    df1['period']='Budget'
  else:
    df1['period']='Actual'
  df1['fin_period']=finyear
  df1=df1[['code', 'description','period','fin_period','year', 'month', 'value']]

  return df1

combined_df=pd.DataFrame()
for k,v in df.items():
  # print(v)??
  combined_df= pd.concat([combined_df,clean_df(v,k)])

combined_df.to_csv('kerk_clean_202311.csv',index=False)

# os.startfile('kerk_clean_202311.csv')

combined_df['year'].unique()