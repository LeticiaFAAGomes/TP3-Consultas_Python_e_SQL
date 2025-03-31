from crud import *
from criacao_tabelas import executar_tabelas
from datetime import datetime

funcionarios, cargos, departamentos, salarios, dependentes = executar_tabelas()

negrito = '\033[1m'
cianoClaro, ciano, branco, azul = '\x1b[38;5;159m', '\x1b[38;5;37m', '\033[37m', '\x1b[38;5;117m'


def formatar(enunciado, cabecalho, rodape, dados, nomes=[], join=False):
    '''
    Esta função retorna uma tabela com os dados alinhados.
    
    Args:
        enunciado(str): Refere-se ao enunciado da atividade.
        cabeçalho(str): Refere-se ao cabeçalho da tabela.
        rodape(str): Refere-se ao rodapé da tabela.
        dados(list): Refere-se aos dados que irão ser imprimidos dentro da tabela.
        nomes(list[str]): Refere-se aos nomes das chaves do dicionario dos dados.
        join(boolean): Refere-se como False quando não é uma junção de tabelas, caso contrário é True.
    '''
    print(f'{negrito}{azul}{enunciado}\n{ciano}{cabecalho}')
    linha = ''
    for dado in dados:
        if (join == True):
            for nome in nomes:
                linha += f'┃ {branco}{getattr(dado, nome , ''):{acharTamanho(dados, nome)}}{ciano}'
            print(f'{linha} ┃')
            linha = ''
        else: print(dado)
    print(rodape)


def acharTamanho(dados, nome):
    '''
    Esta função acha o tamanho máximo que uma string ocupa.
    
    Args:
        dados(list): Refere-se aos dados que irão ter os caracteres contados.
        nome(list[str]): Refere-se a chave do dicionário
    
    Returns:
        int: número máximo de caracteres que dados pode ocupar em uma linha.
    '''
    maximo = max(len(str(getattr(dado, nome))) for dado in dados) + 3 
    if (maximo > len(nome)): return maximo
    
    return len(nome) + 3

# TP1.1 - Listar individualmente as tabelas de: Funcionários, Cargos, Departamentos, Histórico de Salários e Dependentes em ordem crescente. 
tp3_1_funcionarios = consultar_tabelas('SELECT * FROM tb_funcionario ORDER BY nomeFuncionario;', 'Funcionario')
formatar(f'TP3.1 - {cianoClaro}Listar tabela de Funcionários em ordem crescente',
         f'┏{'┅'*79}┓\n┃ {'ID':^2} ┃ {'Cargo':30} ┃ {'idCargo':^8} ┃ {'idDep':4} ┃ {'Salário':6} ┃ {'Nascimento':7} ┃\n┠{'━'*79}┨', 
         f'┗{'━'*79}┛\n', tp3_1_funcionarios)

tp3_1_cargos = consultar_tabelas('SELECT * FROM tb_cargo ORDER BY nomeCargo;', 'Cargo')
formatar(f'TP3.1 - {cianoClaro}Listar tabela de Cargos em ordem crescente', 
         f'┏{'┅'*70}┓\n┃ {'ID':^2} | {'Cargo':30} | {'Salário':^8} | {'Nível':10} | {'Escala':6} ┃\n┠{'━'*70}┨', 
         f'┗{'━'*70}┛\n', tp3_1_cargos)

tp3_1_departamentos = consultar_tabelas('SELECT * FROM tb_departamento ORDER BY nomeDepartamento;', 'Departamento')
formatar(f'TP3.1 - {cianoClaro}Listar tabela de Departamentos em ordem crescente',
         f'┏{'┅'*66}┓\n┃ {'ID':^2} | {'Departamento':30} | {'idGer':^5} | {'Andar':^5} | {'Horário':10} ┃\n┠{'━'*66}┨', 
         f'┗{'━'*66}┛\n', tp3_1_departamentos)

tp3_1_historicosSalariais = consultar_tabelas('SELECT * FROM tb_historicoSalarial ORDER BY idFuncionario, data;', 'HistoricoSalarial')
formatar(f'TP3.1 - {cianoClaro}Listar tabela de Histórico de Salários em ordem crescente',
         f'┏{'┅'*39}┓\n┃ {'ID':^3} | {'idFun':5} | {'Data':^10} | {'Salario':^10} ┃\n┠{'━'*39}┨', 
         f'┗{'━'*39}┛\n', tp3_1_historicosSalariais)

tp3_1_dependentes = consultar_tabelas('SELECT * FROM tb_Dependente ORDER BY nome;', 'Dependente')
formatar(f'TP3.1 - {cianoClaro}Listar tabela de Dependentes em ordem crescente', 
         f'┏{'┅'*87}┓\n┃ {'IdDep':^3} | {'idFun':4} | {'Parentesco':^8} | {'Dependente':30} | {'Nascimento':6} | {'Gênero':10} ┃\n┠{'━'*87}┨', 
         f'┗{'━'*87}┛\n', tp3_1_dependentes)

# TP1.2 - Listar os funcionários, com seus cargos, departamentos e os respectivos dependentes.
tp3_2 = consultar_tabelas("""
        SELECT F.nomeFuncionario AS Funcionario, 
        C.nomeCargo              AS Cargo, 
        C.nivelCargo             AS Nivel, 
        DP.nomeDepartamento      AS Departamento, 
        group_concat(d.nome)     AS Dependentes
        FROM tb_funcionario       F
        JOIN tb_cargo             C   ON F.idCargo = C.idCargo  
        JOIN tb_departamento      DP  ON F.idDepartamento = DP.idDepartamento
        LEFT JOIN tb_dependente   D   ON F.idFuncionario = D.idFuncionario
        GROUP BY F.idFuncionario""", 'Joins')

formatar(f'TP3.2 - {cianoClaro}Listar os funcionários, com seus cargos, departamentos e os respectivos dependentes.',
         f'''┏{'┅'*167}┓\n┃ {'Funcionário':{acharTamanho(tp3_2 , 'Funcionario')}}| {'Cargo':{acharTamanho(tp3_2 , 'Cargo')}}| {'Nível':{acharTamanho(tp3_2 , 'Nivel')
         }}| {'Departamento':{acharTamanho(tp3_2 , 'Departamento')}}| {'Dependente':{acharTamanho(tp3_2 , 'Dependentes')}} ┃\n┠{'━'*167}┨''', 
         f'┗{'━'*167}┛\n', tp3_2, ['Funcionario', 'Cargo', 'Nivel', 'Departamento', 'Dependentes'], True)


def tp3_3():
    # TP3.3 - Listar os funcionários que tiveram aumento salarial nos últimos 3 meses.
    '''
    Esta função encontra os funcionário que tiveram aumento salarial nos últimos 3 meses.
    
    Returns:
        dados(list): Retorna uma lista com os funcionário que tiveram aumento salárial nos últimos 3 meses.
    '''
    dados = []
    for funcionario in funcionarios:
        aumentos = {}
        c = 1
        for salario in salarios:
            diferencaDias = (datetime.strptime('2024-02-10', '%Y-%m-%d') - datetime.strptime(salario['data'], '%Y-%m-%d')).days
            if salario['idFuncionario'] == funcionario['idFuncionario']:
                if diferencaDias <= 92 and len(aumentos) != 4:
                    aumentos['funcionario'] = funcionario['nomeFuncionario']
                    aumentos[f'salario{c}'] = salario["salario"]
                    c +=1
        diferencaSalario = float(aumentos['salario3']) - float(aumentos['salario1'])
        if (diferencaSalario > 0): 
            diferencaSalarios = str(f'{diferencaSalario:.3f}').lstrip('0.')
            dados.append(Joins(funcionario=aumentos['funcionario'], salarioInicio=aumentos['salario1'], salariofinal=aumentos['salario3'], aumentoRS=diferencaSalarios))

    return dados

formatar(f'TP3.3 - {cianoClaro}Listar os funcionários que tiveram aumento salarial nos últimos 3 meses.', 
         f'┏{'┅'*70}┓\n┃ {'Funcionário':{acharTamanho(tp3_3(), 'funcionario')}}| {'Inicio(R$)':{acharTamanho(tp3_3(), 'salarioInicio')}}| {'Final(R$)':{acharTamanho(tp3_3(), 'salariofinal')}}| {'Aumento(R$)':{acharTamanho(tp3_3(), 'aumentoRS')}} ┃\n┠{'━'*70}┨', 
         f'┗{'━'*70}┛\n', tp3_3(), ['funcionario', 'salarioInicio', 'salariofinal', 'aumentoRS'], True)


# TP1.4 - Listar a média de idade dos filhos dos funcionários por departamento. 
tp3_4 = consultar_tabelas('''
        SELECT DP.nomeDepartamento                             AS Departamento, 
        ROUND(AVG(TIMESTAMPDIFF(YEAR, D.idade, CURDATE())),1)  AS Media_Idade
        FROM tb_funcionario  F
        JOIN tb_Departamento DP  ON F.idDepartamento = DP.idDepartamento
        JOIN tb_Dependente   D   ON F.idFuncionario = D.idFuncionario
        WHERE D.parentesco = 'filho'
        GROUP BY DP.nomeDepartamento;''', 'Joins')

formatar(f'TP3.4 - {cianoClaro}Listar a média de idade dos filhos dos funcionários por departamento.',
         f'┏{'┅'*39}┓\n┃ {'Departamento':{acharTamanho(tp3_4 , 'Departamento')}}┃ {'Média de Idade':{acharTamanho(tp3_4 , 'Media_Idade')}} ┃\n┠{'━'*39}┨', 
         f'┗{'━'*39}┛\n',
         tp3_4, ['Departamento', 'Media_Idade'], True)


# TP1.5 - Listar qual estagiário possui filho
tp3_5 = consultar_tabelas('''
        SELECT F.nomeFuncionario  AS Funcionario, 
        C.nivelCargo              AS Nivel, 
        D.nome                    AS Dependente, 
        D.parentesco
        FROM tb_funcionario  F
        JOIN tb_dependente   D    ON F.idFuncionario = D.idFuncionario
        JOIN tb_cargo        C    ON F.idCargo = C.idCargo
        WHERE c.nivelCargo = "Estagiário" AND D.parentesco = "Filho" ''', 'Joins')

formatar(f'TP3.5 - {cianoClaro}Listar qual estagiário possui filho',
        f'┏{'┅'*80}┓\n┃ {'Funcionário':{acharTamanho(tp3_5, 'Funcionario')}}┃ {'Nível':{acharTamanho(tp3_5, 'Nivel')}}┃ {'Dependente':{acharTamanho(tp3_5, 'Dependente')}}┃ {'Parentesco':{acharTamanho(tp3_5, 'parentesco')}} ┃ \n┠{'━'*80}┨', 
        f'┗{'━'*80}┛\n',
        tp3_5, ['Funcionario', 'Nivel', 'Dependente', 'parentesco'], True)


def tp3_6():
    # TP3.6 - Listar o funcionário que teve o salário médio mais alto. 
    '''
    Esta função identifica qual funcionário que teve o salário médio mais alto.
    
    Returns:
        dados(list): Retorna uma lista com o funcionário que teve o salário médio mais alto.
    '''
    dados, salarioMaior, funcionarioMaior = [], 0, {}
    for funcionario in funcionarios:
        qtd, soma = 0, 0
        for salario in salarios:
            if salario['idFuncionario'] == funcionario['idFuncionario']:
                soma += float(salario["salario"])
                qtd +=1
        media = soma / qtd
        if media > salarioMaior:
            salarioMaior = media
            funcionarioMaior['funcionario'] = funcionario['nomeFuncionario']
            funcionarioMaior['media'] = f'{salarioMaior:.3f}'
            
    dados.append(Joins(funcionario=funcionarioMaior['funcionario'], media=funcionarioMaior['media'])) 
   
    return dados

formatar(f'TP3.6 - {cianoClaro}Listar o funcionário que teve o salário médio mais alto', 
        f'┏{'┅'*28}┓\n┃ {'Funcionário':{acharTamanho(tp3_6(), 'funcionario')}}| {'Media(R$)':{acharTamanho(tp3_6(), 'media')}} ┃\n┠{'━'*28}┨', 
        f'┗{'━'*28}┛\n', tp3_6(), ['funcionario','media'], True)


# TP1.7 - Listar o analista que é pai de 2(duas) meninas.
tp3_7 = consultar_tabelas('''
        SELECT F.nomeFuncionario AS Funcionario, 
        COUNT(D.idFuncionario)   AS qtd
        FROM tb_funcionario F
        JOIN tb_cargo C          ON F.idCargo = C.idCargo 
        JOIN tb_dependente D     ON F.idFuncionario = D.idFuncionario
        WHERE C.nivelCargo = 'Analista' 
        AND D.parentesco = 'Filho' 
        AND D.genero = 'Feminino'
        GROUP BY F.idFuncionario
        HAVING qtd = 2;''', 'Joins')

formatar(f'TP3.7 - {cianoClaro}Listar o analista que é pai de 2(duas) meninas.',
        f'┏{'┅'*24}┓\n┃ {'Funcionário':{acharTamanho(tp3_7, 'Funcionario')}}┃ {'Qtd':^{acharTamanho(tp3_7, 'qtd')}} ┃ \n┠{'━'*24}┨', 
         f'┗{'━'*24}┛\n',
         tp3_7, ['Funcionario', 'qtd'], True)

                   
def tp3_8():
    # TP1.8 - Listar o analista que tem o salário mais alto, e que ganhe entre 5000 e 9000. 
    '''
    Esta função identifica qual analista que tem o salário mais alto que ganhe entre 5.000 a 9.000.
    
    Returns:
        dados(list): Retorna uma lista com o nome, nivel e salario do analista que tem o salário mais alto que ganhe entre 5.00 a 9.000
    
    '''
    dados, salarioAnalistaMaior= [], 0
    for funcionario in funcionarios:
        for cargo in cargos:
            if cargo['idCargo'] == funcionario['idCargo'] and cargo['nivelCargo'] == 'Analista':
                salarioReal = float(funcionario['salarioReal'])
                if salarioReal >= 5.000 and salarioReal <= 9.000:
                    if salarioReal > salarioAnalistaMaior:
                        salarioAnalistaMaior = salarioReal
                        analistaMaior = funcionario['nomeFuncionario']
                        analistaMaiorNivel= cargo['nivelCargo']
                        analistaMaiorSalario =  f'{salarioReal:.3f}'
                        
    dados.append(Joins(funcionario=analistaMaior, nivel=analistaMaiorNivel, salarioRS=analistaMaiorSalario))
    
    return dados

formatar(f'TP3.8 - {cianoClaro}Listar o analista que tem o salário mais alto, e que ganhe entre 5000 e 9000.',
        f'┏{'┅'*46}┓\n┃ {'Funcionário':{acharTamanho(tp3_8(), 'funcionario')}}| {'Nível':{acharTamanho(tp3_8(), 'nivel')}}| {'Salário(R$)':{acharTamanho(tp3_8(), 'salarioRS')}} ┃\n┠{'━'*46}┨', 
        f'┗{'━'*46}┛\n', tp3_8(), ['funcionario', 'nivel', 'salarioRS'], True)                    
                

def tp3_9():
    # TP3.9 - Listar qual departamento possui o maior número de dependentes.
    '''
    Esta função identifica qual departamento possui mais dependentes.
    
    Returns:
        dados(list): Retorna uma lista do departamento com mais dependentes e a quantidade.
    '''
    dados, dependentesDepartamento, departamentoMaior = [], {}, 0
    for dependente in dependentes:
        idFuncionario = dependente['idFuncionario']
        
        for funcionario in funcionarios:
            if funcionario['idFuncionario'] == idFuncionario: idDepartamento = funcionario['idDepartamento']
            
        for departamento in departamentos:
            if departamento['idDepartamento'] == idDepartamento: nomeDepartamento = departamento['nomeDepartamento']
            
        if nomeDepartamento not in dependentesDepartamento: dependentesDepartamento[nomeDepartamento] = 0
        dependentesDepartamento[nomeDepartamento] += 1
        
        if (dependentesDepartamento[nomeDepartamento] > departamentoMaior):
            departamentoMaior = dependentesDepartamento[nomeDepartamento]
            departamentoNome = nomeDepartamento
            
    dados.append(Joins(departamento=departamentoNome, qtd=departamentoMaior))
            
    return dados

formatar(f'TP3.9 - {cianoClaro}Listar qual departamento possui o maior número de dependentes.', 
    f'┏{'┅'*24}┓\n┃ {'Departamento':{acharTamanho(tp3_9(), 'departamento')}}| {'Qtd':{acharTamanho(tp3_9(), 'qtd')}} ┃\n┠{'━'*24}┨', f'┗{'━'*24}┛\n',
    tp3_9(), ['departamento','qtd'], True)


def tp3_10():
    # TP1.10 Listar a média de salário por departamento em ordem decrescente.
    '''
    Esta função identifica os salarios médios de cada departamento em ordem decrescente.
    
    Returns:
        dados(list): Retorna uma lista do departamento com mais dependentes e a média salarial.
    '''
    departamentoMaior = []
    for departamento in departamentos:  
        idDepartamento, nomeDepartamento = departamento['idDepartamento'], departamento['nomeDepartamento']  
        soma, qtd = 0 ,0
        
        for funcionario in funcionarios:  
            if funcionario['idDepartamento'] == idDepartamento:  
                salario = float(funcionario['salarioReal'])
                soma += salario  
                qtd += 1  
        if qtd > 0:  
            media = soma / qtd
            departamentoMaior.append(Joins(nomeDepartamento=nomeDepartamento, media=f'{media:.3f}'))

    departamentoMaior.sort(key=lambda x: float(x.media), reverse=True)

    return departamentoMaior

formatar(f'TP3.10 - {cianoClaro}Listar a média de salário por departamento em ordem decrescente.',
    f'┏{'┅'*34}┓\n┃ {'Departamento':{acharTamanho(tp3_10(), 'nomeDepartamento')}}┃ {'Média(R$)':{acharTamanho(tp3_10(), 'media')}} ┃\n┠{'━'*34}┨',f'┗{'━'*34}┛\n', 
    tp3_10(), ['nomeDepartamento','media'], True)

desconectar(conn)
