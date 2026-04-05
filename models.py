import sqlite3


def adicionar_livro(titulo, autor, editora, genero, status, nota = None):
    connection = sqlite3.connect("joyshelf.db")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO livros ("
                   "titulo,"
                   "autor,"
                   "editora,"
                   "genero,"
                   "status,"
                   "nota"
                   ") "
                   "VALUES ("
                   "?,"
                   "?,"
                   "?,"
                   "?,"
                   "?,"
                   "?"
                   ")", (
                   titulo,
                   autor,
                   editora,
                   genero,
                   status,
                   nota
                   ))

    connection.commit()
    connection.close()

    print("🌟 Livro adicionado com sucesso! 🌟")


def listar_todos():
    connection = sqlite3.connect("joyshelf.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * "
                   "FROM livros;")

    lista = cursor.fetchall()
    connection.close()
    return lista


def ordem_alfabetica():
    connection = sqlite3.connect("joyshelf.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * "
                   "FROM livros "
                   "ORDER BY titulo ASC;")

    lista = cursor.fetchall()
    connection.close()
    return lista


def ordem_genero(genero):
    connection = sqlite3.connect("joyshelf.db")
    cursor = connection.cursor()


    cursor.execute("SELECT * "
                   "FROM livros "
                   "WHERE genero = ?", (
                    genero,
                    ))

    lista = cursor.fetchall()
    connection.close()
    return lista


def ordem_editora(editora):
    connection = sqlite3.connect("joyshelf.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * "
                   "FROM livros "
                   "WHERE editora = ?", (
                    editora,
                    ))

    lista = cursor.fetchall()
    connection.close()
    return lista


def ordem_autor(autor):
    connection = sqlite3.connect("joyshelf.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * "
                   "FROM livros "
                   "WHERE autor = ?", (
                    autor,
                    ))

    lista = cursor.fetchall()
    connection.close()
    return lista


def ordem_status_de_leitura(status):
    connection = sqlite3.connect("joyshelf.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * "
                   "FROM livros "
                   "WHERE status = ?", (
                    status,
                    ))

    lista = cursor.fetchall()
    connection.close()
    return lista


def editar_livro(id, titulo = None, autor = None, editora = None, genero = None, status = None, nota = None):
    connection = sqlite3.connect("joyshelf.db")
    cursor = connection.cursor()

    dados_livro = {
        "titulo": titulo,
        "autor": autor,
        "editora": editora,
        "genero": genero,
        "status": status,
        "nota": nota
    }

    campos_validos = []

    for chave, valor in dados_livro.items():
        if valor is not None:
            campos_validos.append((chave, valor))

    campos_set = []

    for campo in campos_validos:
        campos_set.append(campo[0] + " = ?")

    clausula_set = ", ".join(campos_set)

    update_usuario = []

    for campo in campos_validos:
        update_usuario.append(campo[1])

    cursor.execute(f"UPDATE livros "
                   f"SET {clausula_set} "
                   f"WHERE id = ?", (
                    *update_usuario,
                    id,
                    ))

    connection.commit()
    connection.close()

    print("🌟 Edição realizada com sucesso! 🌟")


def excluir_livro(id):
    connection = sqlite3.connect("joyshelf.db")
    cursor = connection.cursor()

    cursor.execute("DELETE "
                   "FROM livros "
                   "WHERE id = ?", (
                    id,
                    ))

    connection.commit()
    connection.close()

    print("🌟 Livro excluído com sucesso! 🌟")