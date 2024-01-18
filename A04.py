# Importando a biblioteca sqlite3
import sqlite3

# Nome do banco de dados
DATABASE = 'livros.db'

# Conectando ao banco de dados
conn = sqlite3.connect(DATABASE)

# Criando um cursor
cursor = conn.cursor()

# Criando a tabela Livros se ela não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Livros(
        id INTEGER PRIMARY KEY,
        titulo TEXT,
        autor TEXT
    )
    ''')

# Inserindo alguns livros na tabela
cursor.execute('INSERT INTO Livros(titulo, autor) VALUES (?,?)', ('1984', 'George Orwell'))
cursor.execute('INSERT INTO Livros(titulo, autor) VALUES (?,?)', ('O Sol é Para Todos', 'Harper Lee'))

# Salvando as alterações
conn.commit()

# Selecionando todos os livros e imprimindo-os
cursor.execute('SELECT * FROM Livros')
for row in cursor.fetchall():
    print(row)
    
# Fechando a conexão
conn.close()