
import pandas as pd
import matplotlib.pyplot as plt

path = r'/Users/javierdiaz/Desktop/report/'

colombia = path+'ODS_CO_256_CO(1)_1595528396.csv'
chile = path+'ODS_CL_260_CL(1)_1595528365.csv'
ecuador = path+'ODS_EC_261_EC(1)_1595528425.csv'
mexico = path+'ODS_MX_257_MX(1)_1595528449.csv'
peru = path+'ODS_PE_262_PE(1)_1595528479.csv'

df_colombia = pd.read_csv(colombia, dtype=str)
df_chile = pd.read_csv(chile, dtype=str)
df_ecuador = pd.read_csv(ecuador, dtype=str)
df_mexico = pd.read_csv(mexico, dtype=str)
df_peru = pd.read_csv(peru, dtype=str)

df_all = pd.concat([
  df_colombia,
  df_chile,
  df_ecuador,
  df_mexico,
  df_peru
])

def tot_register(dataframe):
  return dataframe.shape[0]

tot_co = str(tot_register(df_colombia))
print(tot_co)

#print( df_all.groupby(['iso'])['iso'].count() )
df_colombia['codigoConsultora'].apply( lambda x: str(x).strip().lower() ).to_csv('{}_df_colombia.csv'.format(str(tot_register(df_colombia))), index=False)
df_chile['codigoConsultora'].apply( lambda x: str(x).strip().lower() ).to_csv('{}_df_chile.csv'.format(str(tot_register(df_chile))), index=False)
df_ecuador['codigoConsultora'].apply( lambda x: str(x).strip().lower() ).to_csv('{}_df_ecuador.csv'.format(str(tot_register(df_ecuador))), index=False)
df_mexico['codigoConsultora'].apply( lambda x: str(x).strip().lower() ).to_csv('{}_df_mexico.csv'.format(str(tot_register(df_mexico))), index=False)
df_peru['codigoConsultora'].apply( lambda x: str(x).strip().lower() ).to_csv('{}_df_peru.csv'.format(str(tot_register(df_peru))), index=False)
print( 'Exportado' )

#plt.plot(df_all.groupby(['iso'])['iso'].count())