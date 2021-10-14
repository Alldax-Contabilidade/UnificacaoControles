import pyodbc

banco = pyodbc.connect('DSN=Contabil')
cursor = banco.cursor()

cursor.tables()
rows = cursor.fetchall()
for row in rows:
    print(row.table_name)


# cursor.execute("SELECT * FROM externo.bethadba.EFPARAMETRO_VIGENCIA_IMPOSTOS WHERE codi_emp = 221")
# valores = cursor.fetchall()
#
# for valor in valores:
#     print(valor)
