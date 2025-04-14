import sqlite3

# Conecta ao banco de dados SQLite
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Lista as tabelas do banco de dados
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Exibe as tabelas
for table in tables:
    print(table[0])

# Fecha a conexão
conn.close()
