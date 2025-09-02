import psycopg2

conn = psycopg2.connect(
dbname="banco_dados",
        user="Myriam",
        password="1234",
        host="localhost",
)

cursor = conn.cursor()

cursor.execute('''
      CREATE TABLE IF NOT EXISTS alunos (
          id SERIAL PRIMARY KEY,
          nome VARCHAR(100) NOT NULL,
          telefone CHAR(15) NOT NULL
      )
  ''')

cursor.execute("INSERT INTO alunos (nome, telefone) VALUES (%s, %s)", ("José", "(11)99111-2384"))
cursor.execute("INSERT INTO alunos (nome, telefone) VALUES (%s, %s)", ("Jenifer", "(33)93212-3293"))
conn.commit()

cursor.execute("SELECT * FROM alunos")
registros = cursor.fetchall()

for alunos in registros:
    print(alunos)