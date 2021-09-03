import pandas as pd


df = pd.read_csv("ocorrencia.csv", sep=';', parse_dates=['ocorrencia_dia'])
print(df.ocorrencia_dia.dt.month)

