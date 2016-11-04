# cursor.execute("""
# SELECT name FROM sqlite_master WHERE type='table' ORDER BY name
# """)
#
# print('Tabelas:')
# for tabela in cursor.fetchall():
#     print("%s" % (tabela))

# lendo os dados
# cursor.execute("""
#     SELECT * FROM API_RestFul_persistance;
# """)
#
# for linha in cursor.fetchall():
#     print(linha)
#-------------------------------------------------------------------------------



#--------Lista a quantidade de dados---------------------
r = cursor.execute(
    'SELECT COUNT(*) FROM API_RestFul_persistance')
print("Total de clientes:", r.fetchone()[0])
