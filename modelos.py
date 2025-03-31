ciano, branco =  '\033[36m', '\033[37m'

class Funcionario:
    def __init__(self, idFuncionario, nome, idCargo, idDepartamento, salarioReal, dataNascimento):
        '''
        Esta função inicializa um novo registro de funcionários.
        
        Args:
            idFuncionario(int): Refere-se ao identificador do funcionário.
            nome(str): Refere-se ao nome do funcionário.
            idCargo(int): Refere-se ao identificador do cargo do funcionário.
            idDepartamento(int): Refere-se ao identificador do departamento do funcionário.
            salarioReal(float): Refere-se ao salário real do funcionário.
            dataNascimento(str): Refere-se à data de nascimento do funcionário.
        Returns:
            str: Retorna os dados formatados.
        '''
        self.idFuncionario = idFuncionario
        self.nome = nome
        self.idCargo = idCargo
        self.idDepartamento = idDepartamento
        self.salarioReal = salarioReal
        self.dataNascimento = dataNascimento
        
    def __str__(self):
        '''Retorna de uma string com os dados que foram passados como parâmetro.'''
        return f'┃ {branco}{self.idFuncionario:<2}{ciano} ┃ {branco}{self.nome:30}{ciano} ┃ {branco}{self.idCargo:^8}{ciano} ┃ {branco}{self.idDepartamento:^5}{ciano} ┃ {branco}{self.salarioReal:^7}{ciano} ┃ {branco}{self.dataNascimento}{ciano} ┃'
        
class Cargo:
    def __init__(self, idCargo, nome, salarioBase, nivel, escala):
        '''
        Esta função inicializa um novo registro de cargos.
        
        Args:
            idCargo(int): Refere-se ao identificador do cargo.
            nome(str): Refere-se ao nome do cargo.
            salarioBase(float): Refere-se ao salário base do cargo.
            nivel(str): Refere-se ao nível do cargo
            escala(str): Refere-se à escala do cargo.
            
        Returns:
            str: Retorna os dados formatados.
        '''
        self.idCargo = idCargo
        self.nome = nome
        self.salarioBase = salarioBase
        self.nivel = nivel
        self.escala = escala
        
    def __str__(self):
        '''Retorna de uma string com os dados que foram passados como parâmetro.'''
        return f'┃ {branco}{self.idCargo:<2}{ciano} ┃ {branco}{self.nome:30}{ciano} ┃ {branco}{self.salarioBase:^8}{ciano} ┃ {branco}{self.nivel:10}{ciano} ┃ {branco}{self.escala:^6}{ciano} ┃'
    
class Departamento:
    def __init__(self, idDepartamento, nome, idGerente, andar, horario):
        '''
        Esta função inicializa um novo registro de departamentos.
        
        Args:
        idDepartamento(int): Refere-se ao identificador do departamento.
        nome(str): Refere-se ao nome do departamento.
        idGerente(int): Refere-se ao identificador do gerente do departamento.
        andar(int): Refere-se ao andar do departamento.
        horario(str): Refere-se ao horário de funcionamento do departamento.
            
        Returns:
            str: Retorna os dados formatados.
        '''
        self.idDepartamento = idDepartamento
        self.nome = nome
        self.idGerente = idGerente
        self.andar = andar
        self.horario = horario
        
    def __str__(self):
        '''Retorna de uma string com os dados que foram passados como parâmetro.'''
        return f'┃ {branco}{self.idDepartamento:<2}{ciano} ┃ {branco}{self.nome:30}{ciano} ┃ {branco}{self.idGerente:^5}{ciano} ┃ {branco}{self.andar:^5}{ciano} ┃ {branco}{self.horario:^6}{ciano} ┃'
    
class HistoricoSalarial:
    def __init__(self, idSalarial, idFuncionario, data, salario):
        '''        
        Esta função inicializa um novo registro de históricos salariais.
        
        Args:
            idSalarial(int): Refere-se ao identificador do salário.
            idFuncionario(int): Refere-se ao identificador do funcionário.
            data(str): Refere-se à data que o salário foi pago.
            salario(float): Refere-se ao salário pago para o funcionário.
            
        Returns:
            str: Retorna os dados formatados.
        '''
        self.idSalarial = idSalarial
        self.idFuncionario = idFuncionario
        self.data = data
        self.salario = salario
        
    def __str__(self):
        '''Retorna de uma string com os dados que foram passados como parâmetro.'''
        return f'┃ {branco}{self.idSalarial:<3}{ciano} ┃ {branco}{self.idFuncionario:^5}{ciano} ┃ {branco}{self.data}{ciano} ┃ {branco}{self.salario:^10}{ciano} ┃'
    
class Dependente:
    def __init__(self, idDependente, idFuncionario, parentesco, nome, dataNascimento, genero):
        '''
        Esta função inicializa um novo registro de dependentes.
        
        Args:
            idDependente(int): Refere-se ao identificador do dependente.
            idFuncionario(int): Refere-se ao identificador do funcionário.
            parentesco(str): Refere-se ao parentesco.
            nome(str): Refere-se ao nome do dependente.
            dataNascimento(str): Refere-se à data de nascimento do dependente.
            genero(str): Refere-se ao genero do dependente.
            
        Returns:
            str: Retorna os dados formatados.
        '''
        self.idDependente = idDependente
        self.idFuncionario = idFuncionario
        self.parentesco = parentesco
        self.nome = nome
        self.dataNascimento = dataNascimento
        self.genero = genero
        
    def __str__(self):
        '''Retorna de uma string com os dados que foram passados como parâmetro.'''
        return f'┃ {branco}{self.idDependente :^5}{ciano} ┃ {branco}{self.idFuncionario:^5}{ciano} ┃ {branco}{self.parentesco:^10}{ciano} ┃ {branco}{self.nome:30}{ciano} ┃ {branco}{self.dataNascimento}{ciano} ┃ {branco}{self.genero:10}{ciano} ┃'
    
class Joins:
    def __init__(self, **dados):
        '''
        Esta função inicializa os objetos passados por parâmetros passados por palavras-chaves.
        
        Args:
            **dados(kwargs): Pares chave-valor que identificam os atributos dos objetos passados.
        '''
        for nome, resultado in dados.items():
            setattr(self, nome, resultado)
            