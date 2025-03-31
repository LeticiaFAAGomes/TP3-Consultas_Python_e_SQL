import csv
from conexao_db import *
from modelos import *

conn = conectar()
cursor = conn.cursor()

def ler_dados_csv(arquivo):
    '''
    Esta função lê dados de um arquivo .CSV e os retorna como lista.
    
    Args:
        arquivo(str): Refere-se ao caminho do arquivo .CSV a ser lido.
    
    Returns:
        dados(list[dict]): Retorna uma lista com os dados armazenados no arquivo .CSV.
    
    '''
    with open(f'tabelas\\{arquivo}', mode='r', newline='', encoding='utf-8') as csvfile:
        leitura = csv.DictReader(csvfile)
        dados = [dado for dado in leitura]
        
    return dados

def consultar_tabelas(comando, modelo):
    '''
    Esta função consulta as tabelas do MySQL a partir de um comando.
    
    Args:
        comando(str): Refere-se ao comando SQL.
        modelo(str): Refere-se ao modelo da classe.
    
    Returns:
        lista(list): Retorna o resultado do comando SQL.
    
    '''
    try:
        lista = []
        classe = globals().get(modelo)
        cursor.execute(comando)
        informacoes = cursor.fetchall()
        nomeColunas = [nome[0] for nome in cursor.description]
        
        for informacao in informacoes:
            if (modelo == 'Joins'):
                dados = {coluna: resultado for coluna, resultado in zip(nomeColunas, informacao)}
                lista.append(classe(**dados))
            else:
                dados = [dado for dado in informacao]
                lista.append(classe(*dados))
        
    except Exception as ex:
        print(ex)
    
    return lista
            

def criar_tabelas(comando):
    '''
    Esta função cria tabelas no MySQL a partir de um comando.
    
    Args:
        comando(str): Refere-se à um comando SQL.
    '''
    try:
        cursor.execute(comando)
            
    except Exception as ex:
        print(ex)


def criar_insert(comando, valores):
    '''
    Esta função insere INSERTs em uma tabela no MySQL a partir de um comando.
    
    Args:
        comando(str): Refere-se à um comando SQL.
        valores(str): Refere-se aos dados à serem adicionados na tabela.
    '''
    try:
        cursor.executemany(comando, valores)
                
    except Exception as ex:
        print(ex)
    