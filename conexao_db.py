import mysql.connector

def conectar():
    '''
    Esta função faz com que o arquivo se conecte ao banco de dados MySQL 
    a partir do host, usuário, senha e base de dados inseridas corretamente.
    
    Returns:
        conn(mysql.connector.connection.MySQLConnection) = Refere-se à uma instância para a 
                                                           conexão ativa com o servidor do MySQL.
    '''
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
        )
        return conn
    except Exception as ex:
        print(ex)
        exit()

def desconectar(conn):
    '''Esta função faz com que o arquivo salve as alterações e se desconecte do banco de dados MySQL.'''
    if (conn):
        conn.commit()
        conn.close()
 
        
        
        