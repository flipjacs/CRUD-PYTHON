import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='bdyoutube',
)

cursor = conexao.cursor() # Execução da conexao

# CRUD

# comandos essencias:
# comando = 'comandosql'
# cursor.execute (comando) #executar comando
# conexao.commit() #edita o banco de dados: escrita de dados
# resultado = cursor.fetchall # somente leitura do banco

#CREATE
nome_produto = "chocolate"
valor = 15
comando = f'INSERT INTO Vendas(nome_produto,valor) values ("{nome_produto}",{valor})'
cursor.execute(comando)
conexao.commit()

#READ

comando = f'SELECT * FROM Vendas'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)

#UPDATE

valor= 6
nome_produto = "todynho"
comando = f'update Vendas SET valor = {valor} WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

# DELETE

nome_produto = "todynho"
comando = f'Delete From Vendas WHERE nome_produto = "{nome_produto}"'
cursor.execute(comando)
conexao.commit()

# fechar conexao (no fim do codigo)
cursor.close() 
conexao.close()