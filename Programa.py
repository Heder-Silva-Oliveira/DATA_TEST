import pandas as pd
import pandera as pa

valores_ausentes = ['*', '###!', '####', '****', '*****', 'NULL']
df = pd.read_csv("ocorrencia.csv", sep=';', parse_dates=['ocorrencia_dia'], dayfirst=True, na_values=valores_ausentes)
df.pop('ocorrencia_saida_pista')
df.pop('total_aeronaves_envolvidas')
df.pop('codigo_ocorrencia1')
df.pop('codigo_ocorrencia3')
df.pop('codigo_ocorrencia4')
df.pop('ocorrencia_longitude')
df.pop('ocorrencia_latitude')
df.pop('ocorrencia_pais')
df.pop('investigacao_aeronave_liberada')
df.pop('investigacao_status')
df.pop('divulgacao_relatorio_numero')
df.pop('divulgacao_dia_publicacao')
df.pop('divulgacao_relatorio_publicado')

schema = pa.DataFrameSchema(
    columns={
        "codigo_ocorrencia": pa.Column(pa.Int),
        "codigo_ocorrencia2": pa.Column(pa.Int),
        "ocorrencia_classificacao": pa.Column(pa.String),
        "ocorrencia_cidade": pa.Column(pa.String),
        "ocorrencia_uf": pa.Column(pa.String, pa.Check.str_length(2,2), nullable=True),
        "ocorrencia_aerodromo": pa.Column(pa.String, nullable=True),
        "ocorrencia_dia": pa.Column(pa.DateTime),
        "ocorrencia_hora": pa.Column(pa.String, pa.Check.str_matches(r'^([0-1]?[0-9]|[2][0-3]):([0-5][0-9])(:[0-5][0-9])?$'), nullable=True),
        "total_recomendacoes": pa.Column(pa.Int)
    }
)

schema.validate(df)
#print(df.isnull().sum())

