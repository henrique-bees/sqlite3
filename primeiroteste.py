import sqlite3 as sq

conexao = sq.connect("teste-sqlite3/bancocalendario.db")
cursor = conexao.cursor()
cursor.execute("""DROP TABLE IF EXISTS usuarios""")
cursor.execute("""CREATE TABLE usuarios (
               id INTEGER PRIMARY KEY,
               nome TEXT,
               senha INTEGER
               )""")
cursor.execute("CREATE INDEX numero ON usuarios(1)")
cursor.execute("INSERT INTO usuarios (nome, senha) VALUES (?, ?)", ("henrique", 1234))
cursor.execute("SELECT nome, senha FROM usuarios")
registros = cursor.fetchall()

print(registros)
conexao.commit()
conexao.close()
