from art import logo
from prettytable import PrettyTable
from models import (adicionar_livro, listar_todos, ordem_alfabetica, ordem_genero, ordem_editora, ordem_autor,
                    ordem_status_de_leitura, editar_livro, excluir_livro)
from database import iniciar_banco


def info_livro(filtro):
    table = PrettyTable()
    table.field_names = ("ID", "Título", "Autor(a)", "Editora", "Gênero", "Status", "Nota")
    for livro in filtro:
        table.add_row([f"{livro[0]}", f"{livro[1]}", f"{livro[2]}", f"{livro[3]}", f"{livro[4]}", f"{livro[5]}", f"{livro[6]}"])
    print(table)

stt_leitura = {
    1: "Quero ler",
    2: "Lendo",
    3: "Lido"
}

iniciar_banco()

print(logo)
print("Seja bem-vindo(a) ao JoyShelf! 🌟\nAqui pode organizar e encontrar todas as suas leituras")

sair = False

while not sair:
    print("Escolha uma das opções: ")
    print("1. Adicionar livro \n"
          "2. Filtrar livros \n"
          "3. Editar livro \n"
          "4. Excluir livro \n"
          "5. Sair")
    try:
        escolha = int(input("Opção: "))

        if escolha < 1 or escolha > 5:
            print("Esta opção não está disponível 😕. Tente novamente.")
            print("\n" * 5)
        else:
            if escolha == 1:
                print("Precisamos que insira algumas informações sobre o livro para organizar sua prateleira! 😄📒")
                titulo = input("Título do livro: ").lower()
                autor = input("Nome do(a) autor(a): ").lower()
                editora = input("Nome da editora: ").lower()
                genero = input("Gênero: ").lower()
                status = int(input("Indique o status da leitura: \n1. Quero ler \n2. Lendo \n3. Lido\n"))
                if status < 1 or status > 3:
                    print("Esta opção não está disponível 😕. Tente novamente.")
                    print("\n" * 5)
                else:
                    status_db = stt_leitura[status]

                    if status == 3:
                        nota = float(input("Avaliação: "))
                    else:
                        nota = None

                    adicionar_livro(titulo= titulo, autor= autor, editora= editora, genero= genero, status= status_db, nota= nota)

            elif escolha == 2:
                print("1. Listar todos\n"
                      "2. Ordem alfabética\n"
                      "3. Gênero\n"
                      "4. Editora\n"
                      "5. Autor\n"
                      "6. Status de leitura")

                try:
                    filtrar_livro = int(input("Filtrar por: "))
                    if filtrar_livro < 1 or filtrar_livro > 6:
                        print("Esta opção não está disponível 😕. Tente novamente.")
                        print("\n" * 5)
                    else:
                        if filtrar_livro == 1:
                            filtrar_todos = listar_todos()
                            if not filtrar_todos:
                                print("A estante de livros está vazia!")
                            else:
                                info_livro(filtrar_todos)

                        elif filtrar_livro == 2:
                            filtrar_alfabetica = ordem_alfabetica()
                            if not filtrar_alfabetica:
                                print("A estante de livros está vazia!")
                            else:
                                info_livro(filtrar_alfabetica)

                        elif filtrar_livro == 3:
                            filtrar_genero = str(input("Gênero: ")).lower()
                            genero_db = ordem_genero(filtrar_genero)
                            if not genero_db:
                                print("Não há nenhum livro com este gênero")
                            else:
                                info_livro(genero_db)

                        elif filtrar_livro == 4:
                            filtrar_editora = str(input("Editora: ")).lower()
                            editora_db = ordem_editora(filtrar_editora)
                            if not editora_db:
                                print("Não há nenhum livro com esta editora")
                            else:
                                info_livro(editora_db)

                        elif filtrar_livro == 5:
                            filtrar_autor = str(input("Autor(a): ")).lower()
                            autor_db = ordem_autor(filtrar_autor)
                            if not autor_db:
                                print("Não há nenhum livro com este(a) autor(a)")
                            else:
                                info_livro(autor_db)

                        elif filtrar_livro == 6:
                            try:
                                filtrar_status = int(input("Status: \n1. Quero ler \n2. Lendo \n3. Lido\n"))
                                if filtrar_status < 1 or filtrar_status > 3:
                                    print("Esta opção não está disponível 😕. Tente novamente.")
                                    print("\n" * 5)
                                else:
                                    stt_leitura_dic = stt_leitura[filtrar_status]
                                    filtrar_stt_db = ordem_status_de_leitura(stt_leitura_dic)
                                    if not filtrar_stt_db:
                                        print("Não há nenhum livro com este status.")
                                    else:
                                        info_livro(filtrar_stt_db)
                            except ValueError:
                                print("Esta opção não está disponível 😕. Tente novamente.")
                                print("\n" * 5)

                except ValueError:
                    print("Esta opção não está disponível 😕. Tente novamente.")
                    print("\n" * 5)

            elif escolha == 3:
                try:
                    estante_de_livros = listar_todos()
                    if not estante_de_livros:
                        print("A estante de livros está vazia!")
                    else:
                        info_livro(estante_de_livros)
                        id_livro_para_editar = int(input("Qual livro deseja editar? Indique o id correspondente: "))
                        print("1. Título \n"
                              "2. Autor(a) \n "
                              "3. Editora \n"
                              "4. Gênero \n"
                              "5. Status \n"
                              "6. Nota \n")
                        editar_item = int(input("Qual item deseja editar?: "))

                        if editar_item < 1 or editar_item > 6:
                            print("Esta opção não está disponível 😕. Tente novamente.")
                            print("\n" * 5)
                        else:
                            if editar_item == 1:
                                novo_valor = input("Insira o título: ").lower()
                                editar_livro(id= id_livro_para_editar, titulo= novo_valor)

                            elif editar_item == 2:
                                novo_valor = input("Insira o(a) autor(a): ").lower()
                                editar_livro(id= id_livro_para_editar, autor= novo_valor)

                            elif editar_item == 3:
                                novo_valor = input("Insira a editora: ").lower()
                                editar_livro(id= id_livro_para_editar, editora= novo_valor)

                            elif editar_item == 4:
                                novo_valor = input("Insira o gênero: ").lower()
                                editar_livro(id= id_livro_para_editar, genero= novo_valor)

                            elif editar_item == 5:
                                novo_valor = int(input("Indique o status da leitura: \n1. Quero ler \n2. Lendo \n3. Lido\n"))
                                if novo_valor < 1 or novo_valor > 3:
                                    print("Esta opção não está disponível 😕. Tente novamente.")
                                    print("\n" * 5)
                                else:
                                    stt_leitura_dic = stt_leitura[novo_valor]
                                    editar_livro(id= id_livro_para_editar, status= stt_leitura_dic)

                            elif editar_item == 6:
                                novo_valor = float(input("Insira a nota:"))
                                editar_livro(id= id_livro_para_editar, nota= novo_valor)

                except ValueError:
                    print("Esta opção não está disponível 😕. Tente novamente.")
                    print("\n" * 5)

            elif escolha == 4:
                try:
                    estante_de_livros = listar_todos()
                    if not estante_de_livros:
                        print("A estante de livros está vazia!")
                    else:
                        info_livro(estante_de_livros)
                        deletar_livro = int(input("Qual livro deseja excluir (informe o ID): "))

                        excluir_livro(deletar_livro)

                except ValueError:
                    print("Esta opção não está disponível 😕. Tente novamente.")
                    print("\n" * 5)

            elif escolha == 5:
                sair = True

    except ValueError:
        print("Esta opção não está disponível 😕. Tente novamente.")
        print("\n" * 5)

