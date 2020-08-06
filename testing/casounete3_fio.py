#pip install xlrd

import pandas as pd
import matplotlib.pyplot as plt

path = r'/Users/javierdiaz/Desktop/report/'

excell = path+'ID CS LISTA CARLOS Q.xlsx'

xls = pd.ExcelFile(excell)
print( xls.sheet_names )

def totLongCod(pais):
  if pais == 'PE':
    longitud = 9
  elif pais == 'MX':
    longitud = 7
  elif pais == 'EC':
    longitud = 7
  elif pais == 'CO':
    longitud = 10
  elif pais == 'CL':
    longitud = 7
  return longitud

def totRegister(dataframe):
  return dataframe.shape[0]

df = pd.read_excel(excell, sheet_name="Consultoras que no estan cargad", dtype=str, names={'columna1'})
df['codebelista'] = df['columna1'].str.rpartition('_')[0].apply( lambda x: str(x).strip().lower() )
df['codpais'] = df['columna1'].str.rpartition('_')[2].apply( lambda x: str(x).strip().upper() )

print( df.codpais.unique() )


#Export
for i in df.codpais.unique():
  df[ df.codpais == i ]['codebelista'].apply( lambda x: str(x.zfill(totLongCod(i))) ).to_csv('fio/{}_df_{}_fio.csv'.format( str(totRegister(df[ df.codpais == i ])), i), index=False)
  print("Finalizado pais : {}".format(i))

#Antes  XD
# df[ df.codpais == 'PE' ]['codebelista'].apply( lambda x: str(x.zfill(totLongCod('PE'))) ).to_csv('fio/{}_df_pe_fio.csv'.format(str(totRegister(df[ df.codpais == 'PE' ]))), index=False)
# df[ df.codpais == 'EC' ]['codebelista'].apply( lambda x: str(x.zfill(totLongCod('EC'))) ).to_csv('fio/{}_df_ec_fio.csv'.format(str(totRegister(df[ df.codpais == 'EC' ]))), index=False)
# df[ df.codpais == 'MX' ]['codebelista'].apply( lambda x: str(x.zfill(totLongCod('MX'))) ).to_csv('fio/{}_df_mx_fio.csv'.format(str(totRegister(df[ df.codpais == 'MX' ]))), index=False)
# df[ df.codpais == 'CL' ]['codebelista'].apply( lambda x: str(x.zfill(totLongCod('CL'))) ).to_csv('fio/{}_df_cl_fio.csv'.format(str(totRegister(df[ df.codpais == 'CL' ]))), index=False)
# df[ df.codpais == 'CO' ]['codebelista'].apply( lambda x: str(x.zfill(totLongCod('CO'))) ).to_csv('fio/{}_df_co_fio.csv'.format(str(totRegister(df[ df.codpais == 'CO' ]))), index=False)


print( df.head(10) )
#df = pd.read_csv(excell)