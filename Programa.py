import pandas as pd
import pandera as pa


df = pd.read_csv("ocorrencia.csv", sep=';', parse_dates=['ocorrencia_dia'], dayfirst=True)
df.pop('ocorrencia_saida_pista')
df.pop('total_aeronaves_envolvidas')

schema = pa.DataFrameSchema(
    columns={
        "codigo_ocorrencia":pa.Column(pa.Int)
    }
)
print(schema.validate(df))
