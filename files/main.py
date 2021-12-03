import sqlite3
import pandas as pd

connection = sqlite3.connect('eleflow_database')
cursor = connection.cursor()

query = """
    CREATE TABLE IF NOT EXISTS pib(
        tipo_valor varchar(30), 
        ramo varchar(30), 
        tipo_setor varchar(30), 
        ano integer,
         valor_pib numeric(14,2)) 
"""

query2 = """
    CREATE TABLE IF NOT EXISTS producao(
        uf varchar(30),
        ano integer,
        mes varchar(20),
        atributo varchar(30),
        valor numeric(14,2))
"""

df_pib = pd.read_excel('data/PIB_Cepea.xlsx', sheet_name='PIB', header=6, index_col=0)