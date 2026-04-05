# Joyshelf ☀️

Sistema desenvolvido em Python e SQLite para registro e gerenciamento de livros, com o objetivo de permitir que o 
usuário mantenha uma estante virtual.

## Funcionalidades

| # | Funcionalidade | Descrição |
|---|----------------|-----------|
| 1 | Adicionar livro | Registra um novo livro |
| 2 | Filtrar livros | Filtra por todos, ordem alfabética, gênero, editora, autor(a) e status |
| 3 | Editar livro | Edita as informações de um livro |
| 4 | Excluir livro | Remove o livro desejado |

## Tecnologias utilizadas

- Python 
- SQLite 
- PrettyTable (formatação de tabelas no terminal)

## Como executar

1. Clone o repositório:
```bash
git clone https://github.com/saemiuyeda/Joyshelf.git
```
2. Acesse a pasta do projeto:
```bash
cd Joyshelf
```
3. Instale a biblioteca prettytable:
```bash
pip install prettytable
```
4. Execute o programa:
```bash
python main.py
```

## Conceitos aplicados

### Python

- Manipulação de banco de dados com sqlite3
- Manipulação de dicionários
- Funções reutilizáveis
- Método .items() para iteração em pares do dicionário
- Método .append() para adicionar elementos à lista
- Método .join() para transformar lista de strings em uma única string
- Laço for
- Laço `while` com controle de fluxo
- Estruturas condicionais `if/elif/else`
- Tratamento de exceções com `try/except`
- Formatação com f-strings

### SQL

#### Operações CRUD
  - CREATE TABLE IF NOT EXISTS
  - INSERT INTO
  - SELECT
  - UPDATE
  - DELETE
#### Filtragem e ordenação dos dados
  - WHERE
  - ORDER BY