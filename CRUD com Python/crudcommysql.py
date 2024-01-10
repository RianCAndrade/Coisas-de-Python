import mysql.connector

#Estabelecendo a conexao com o banco de dados MySQL

conexao = mysql.connector.connect(
    host = 'localhost', #local onde ta o banco de dados
    user = 'root', #usuario do MySQL
    password = '', #senha do MySQL 
    database = 'academia', # Banco de dados que sera utilizado
)

cursor = conexao.cursor()

#CRUD:

#CREATE Exemplo:

'''
nome = "Rafaela Santos"
valor = "69.99"
inserir = f'insert into clientes (nome, valorpago) values ("{nome}", "{valor}")'
cursor.execute(inserir)
conexao.commit()
'''

#READ Exemplo:
'''
ler = 'select * from clientes'
cursor.execute(ler)
resp = cursor.fetchall()
print(resp)
'''

#UPDATE Exemplo:
'''
atualizar = "69,00"
id = "7"
att = f'update clientes set valorpago = "{atualizar}" where idcli = "{id}"'
cursor.execute(att)
conexao.commit()
'''

#DELETE Exemplo:

'''
onde = "11"
dell = f'delete from clientes where idcli = "{onde}"'
cursor.execute(dell)
conexao.commit()
'''

#fechando a conexao e o cursor 
cursor.close()
conexao.close()
