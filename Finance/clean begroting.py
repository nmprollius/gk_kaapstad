import os
import pandas as pd
import numpy as np

df=pd.read_excel('Begroting 2024.xlsx',sheet_name=['2024 Begroting', '2023 Begroting'])
# df=df['2024 Begroting']


def getdata(k,df):
    
  # Get clm names
  df.columns=df.iloc[1]
  df.columns=df.columns.str.strip().str.lower().str.replace(' ','')

  #  Remove lows
  df=df[3:]

  df=df.dropna(subset='pastel')[['pastel','begroting']]
  df['year']=k

  return df

begroting=pd.DataFrame()
for k,v in df.items():
  begroting=pd.concat([begroting, getdata(k,v)])

ic_codes=['1000/000','1100/000','1150/000','1150/010','1150/020','1150/030','1150/040','1155/000','1175/000','1200/000','1200/010','1200/011','1300/000','2750/000']

begroting.begroting= np.where(begroting.pastel.isin(ic_codes),begroting.begroting,begroting.begroting*-1)

m={
'2024 Begroting':2024,
'2023 Begroting':2023
}
begroting.year=begroting.year.map(m)

begroting.to_excel('begroting_clean.xlsx',index=False)

os.startfile('begroting_clean.xlsx')