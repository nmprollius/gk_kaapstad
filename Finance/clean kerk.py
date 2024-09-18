import os
import pandas as pd
import numpy as np

# os.startfile(os.getcwd())

df=pd.read_excel('TB Kerk.xlsx',sheet_name=None,skiprows=2,skipfooter=1)



def get_dfs(k,df):
  # Clean columns    
  df.rename(columns={'Unnamed: 2':'description'},inplace=True)
  df.columns = [i.lower().strip().replace(' ','_') for i in df.columns]

  df['year']=k

  # get index positions

  df1_end=df[df['account'].isna()].iloc[0].name
  df2_start=df[df['account'].isna()].iloc[2].name

  # Split TB and Income statement
  tb_df=df.loc[0:df1_end].reset_index(drop=True).copy()
  #Create single clm
  c=tb_df.dr.isna()
  tb_df['val']=np.where(c,tb_df.cr*-1,tb_df.dr)

  ic_df=df.loc[df2_start:].reset_index(drop=True).copy()
   #Create single clm
  c=ic_df.dr.isna()
  ic_df['val']=np.where(c,ic_df.cr,ic_df.dr*-1)

  return tb_df, ic_df


tb=pd.DataFrame()
ic=pd.DataFrame()
for k,v in df.items():
  a,b=get_dfs(k,v)
  tb=pd.concat([tb,a])
  ic=pd.concat([ic,b])


ic_codes=['1000/000','1100/000','1150/000','1150/010','1150/020','1150/030','1150/040','1155/000','1175/000','1200/000','1200/010','1200/011','1300/000','2750/000']

ic['account group']=np.where(ic['account'].isin(ic_codes),'Income','Expenses')

tb.to_excel('tb.xlsx',index=False)
ic.to_excel('ic.xlsx',index=False)

# os.startfile('tb.xlsx')
os.startfile('tb.xlsx')