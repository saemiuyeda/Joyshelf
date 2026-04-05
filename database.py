import sqlite3

def iniciar_banco():
    connection = sqlite3.connect("joyshelf.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS livros ("
                   "id INTEGER PRIMARY KEY,"
                   "titulo TEXT NOT NULL,"
                   "autor TEXT NOT NULL,"
                   "editora TEXT NOT NULL,"
                   "genero TEXT,"
                   "status TEXT NOT NULL,"
                   "nota REAL"
                   ");")

    connection.commit()
    connection.close()