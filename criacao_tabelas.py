from crud import *

cursor.execute('CREATE DATABASE IF NOT EXISTS db_empresa_tech;')
cursor.execute('USE db_empresa_tech;')

def executar_tabelas():
    '''
    Esta função cria todas as tabelas armazenadas nos arquivos .CSV na pasta tabelas e depois insere os dados nelas.
    
    Returns:
        lists:
            funcionarios(list[dict]): dados de funcionarios que estavam armazenados em tb_funcionario.csv;
            cargos(list[dict]): dados de cargos que estavam armazenados em tb_cargo.csv;
            departamentos(list[dict]): dados de departamentos que estavam armazenados em tb_departamento.csv;
            salarios(list[dict]): dados de salários que estavam armazenados em tb_historicoSalarial.csv;
            dependentes(list[dict]): dados de dependentes que estavam armazenados em tb_dependente.csv;
    ''' 
    
    criar_tabelas('''
        CREATE TABLE IF NOT EXISTS tb_Cargo (
            
            idCargo      INTEGER PRIMARY KEY AUTO_INCREMENT,
            nomeCargo    VARCHAR(30),
            salarioBase  DECIMAL(7,3),
            nivelCargo   VARCHAR(30),
            escala       VARCHAR(30)
        );
    ''')

    criar_tabelas('''
        CREATE TABLE IF NOT EXISTS tb_Departamento (
            
            idDepartamento        INT PRIMARY KEY AUTO_INCREMENT,
            nomeDepartamento      VARCHAR(30),
            idGerente             INT,
            andarDepartamento     INT,
            horarioFuncionamento  VARCHAR(30)
        );    
    ''')

    criar_tabelas('''
        CREATE TABLE IF NOT EXISTS tb_Funcionario (
            
            idFuncionario    INT PRIMARY KEY AUTO_INCREMENT,
            nomeFuncionario  VARCHAR(50),
            idCargo          INT,
            idDepartamento   INT,
            salarioReal      DECIMAL(7,3),
            dataNascimento   DATE,
            
            FOREIGN KEY (idCargo) REFERENCES tb_Cargo(idCargo),
            FOREIGN KEY (idDepartamento) REFERENCES tb_Departamento(idDepartamento)
        );
    ''')

    criar_tabelas('''
        CREATE TABLE IF NOT EXISTS tb_historicoSalarial (
            
            idSalarial     INT PRIMARY KEY AUTO_INCREMENT,
            idFuncionario  INT,
            data           DATE,
            salario        DECIMAL(7,3),
            
            FOREIGN KEY (idFuncionario) REFERENCES tb_Funcionario(idFuncionario)
        );
    ''')

    criar_tabelas('''
        CREATE TABLE IF NOT EXISTS tb_Dependente (
        
            idDependente   INT PRIMARY KEY AUTO_INCREMENT,
            idFuncionario  INT,
            parentesco     VARCHAR(10),
            nome           VARCHAR(50),
            idade          DATE,
            genero         VARCHAR(15),
            
            FOREIGN KEY (idFuncionario) REFERENCES tb_Funcionario(idFuncionario)
        );
    ''')
             
    funcionarios = ler_dados_csv('tb_funcionario.csv')
    cargos = ler_dados_csv('tb_cargo.csv')
    departamentos = ler_dados_csv('tb_departamento.csv')
    salarios = ler_dados_csv('tb_historicoSalarial.csv')
    dependentes = ler_dados_csv('tb_dependente.csv')


    criar_insert('INSERT IGNORE INTO tb_Cargo(idCargo, nomeCargo, salarioBase, nivelCargo, escala) VALUES(%(idCargo)s, %(nomeCargo)s, %(salarioBase)s, %(nivelCargo)s, %(escala)s);', 
                        [{'idCargo':cargo['idCargo'],
                        'nomeCargo':cargo['nomeCargo'], 
                        'salarioBase':cargo['salarioBase'], 
                        'nivelCargo':cargo['nivelCargo'], 
                        'escala':cargo['escala']} for cargo in cargos])

    criar_insert('''INSERT IGNORE INTO tb_Departamento(idDepartamento, nomeDepartamento, idGerente, andarDepartamento, horarioFuncionamento) 
                    VALUES(%(idDepartamento)s, %(nomeDepartamento)s, %(idGerente)s, %(andarDepartamento)s, %(horarioFuncionamento)s);''', 
                        [{'idDepartamento':departamento['idDepartamento'],
                        'nomeDepartamento':departamento['nomeDepartamento'], 
                        'idGerente':departamento['idGerente'], 
                        'andarDepartamento':departamento['andarDepartamento'], 
                        'horarioFuncionamento':departamento['horarioFuncionamento']} for departamento in departamentos])

    criar_insert('INSERT IGNORE INTO tb_Funcionario(idFuncionario, nomeFuncionario, idCargo, idDepartamento, salarioReal, dataNascimento) VALUES(%(idFuncionario)s, %(nomeFuncionario)s, %(idCargo)s, %(idDepartamento)s, %(salarioReal)s, %(dataNascimento)s);', 
                        [{'idFuncionario':funcionario['idFuncionario'],
                        'nomeFuncionario':funcionario['nomeFuncionario'], 
                        'idCargo':funcionario['idCargo'], 
                        'idDepartamento':funcionario['idDepartamento'], 
                        'salarioReal':funcionario['salarioReal'], 
                        'dataNascimento':funcionario['dataNascimento']} for funcionario in funcionarios])

    criar_insert('''INSERT IGNORE INTO tb_historicoSalarial(idSalarial, idFuncionario, data, salario) 
                    VALUES(%(idSalarial)s, %(idFuncionario)s, %(data)s, %(salario)s);''', 
                        [{'idSalarial':historicoSalarial['idSalarial'],
                        'idFuncionario':historicoSalarial['idFuncionario'], 
                        'data':historicoSalarial['data'], 
                        'salario':historicoSalarial['salario']} for historicoSalarial in salarios])

    criar_insert('''INSERT IGNORE INTO tb_Dependente(idDependente, idFuncionario, parentesco, nome, idade, genero) 
                    VALUES(%(idDependente)s, %(idFuncionario)s, %(parentesco)s, %(nome)s, %(idade)s, %(genero)s);''', 
                        [{'idDependente':dependente['idDependente'],
                        'idFuncionario':dependente['idFuncionario'], 
                        'parentesco':dependente['parentesco'], 
                        'nome':dependente['nome'], 
                        'idade':dependente['idade'],
                        'genero':dependente['genero']} for dependente in dependentes])
    
    return funcionarios, cargos, departamentos, salarios, dependentes
