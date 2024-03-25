import sqlite3 as conector

try:
    conexao = conector.connect("BancoDeDados.db")
    cursor = conexao.cursor()

    comando = ('''CREATE TABLE TabelaExemplo(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        email TEXT
    );''')

    cursor.execute(comando)
    conexao.commit()

    print("Aguarde...")

except conexao.DatabaseError as err:
    print("Erro de Banco de Dados, tente novamente.\n Erro:", err)

finally:
    if conexao:
        cursor.close()
        conexao.close()
        print("Fim da conexao com o Banco de Dados.")
