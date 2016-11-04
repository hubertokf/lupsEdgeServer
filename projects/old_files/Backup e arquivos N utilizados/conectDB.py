# 06_read_data.py
import sqlite3

conn = sqlite3.connect('../../lupsEdgeServer/db.sqlite3')
cursor = conn.cursor()



# def localizar_cliente(id):
#     r = cursor.execute(
#         'SELECT * FROM API_RestFul_persistance WHERE publisher = ?', (id,))
#     for cliente in r.fetchall():
#         print(cliente)
#
# localizar_cliente(0)

cursor.execute("""
UPDATE API_RestFul_persistance
SET publisher = ?
WHERE id = ?
""", (1, 571))

conn.commit()

conn.close()
