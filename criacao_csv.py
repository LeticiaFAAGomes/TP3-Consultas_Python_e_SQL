import csv

funcionarios, cargos, departamentos, historicoSalarial, dependentes = [], [], [], [], []

def addFuncionario(idFuncionario, nomeFuncionario, idCargo, idDepartamento, salarioReal, dataNascimento):
    '''
    Esta função adiciona dados de um funcionario para a lista funcionarios.
    
    Args:
        idFuncionario(int): Refere-se ao identificador do funcionário.
        nomeFuncionario(str): Refere-se ao nome do funcionário.
        idCargo(int): Refere-se ao identificador do cargo do funcionário.
        idDepartamento(int): Refere-se ao identificador do departamento do funcionário.
        salarioReal(float): Refere-se ao salario real do funcionário.
        dataNascimento(str): Refere-se à data de nascimento do funcionario.
    '''
    funcionarios.append({'idFuncionario':idFuncionario, 
                         'nomeFuncionario':nomeFuncionario, 
                         'idCargo': idCargo, 
                         'idDepartamento': idDepartamento, 
                         'salarioReal': salarioReal, 
                         'dataNascimento': dataNascimento})
    
def addCargo(idCargo, nomeCargo, salarioBase, nivelCargo, escala):
    '''
    Esta função adiciona dados de um cargo para a lista cargos.
    
    Args:
        idCargo(int): Refere-se ao identificador do cargo.
        nomeCargo(str): Refere-se ao nome do cargo.
        salarioBase(float): Refere-se ao salário base do cargo.
        nivelCargo(str): Refere-se ao nível do cargo
        escala(str): Refere-se à escala do cargo.
    '''
    cargos.append({'idCargo':idCargo,
                   'nomeCargo':nomeCargo,
                   'salarioBase':salarioBase,
                   'nivelCargo':nivelCargo,
                   'escala':escala})
    
def addDepartamento(idDepartamento, nomeDepartamento, idGerente, andarDepartamento, horarioFuncionamento):
    '''
    Esta função adiciona dados de um departamento para a lista `departamentos`.
    
    Args:
        idDepartamento(int): Refere-se ao identificador do departamento.
        nomeDepartamento(str): Refere-se ao nome do departamento.
        idGerente(int): Refere-se ao identificador do gerente do departamento.
        andarDepartamento(int): Refere-se ao andar do departamento.
        horarioFuncionamento(str): Refere-se ao horário de funcionamento do departamento.
    '''
    departamentos.append({'idDepartamento':idDepartamento,
                          'nomeDepartamento':nomeDepartamento,
                          'idGerente':idGerente,
                          'andarDepartamento':andarDepartamento,
                          'horarioFuncionamento':horarioFuncionamento})
    
def addHistoricoSalarial(idSalarial, idFuncionario, data, salario):
    '''
    Esta função adiciona dados de um histórico de salário para a lista `historicoSalarial`.
    
    Args:
        idSalarial(int): Refere-se ao identificador do salário.
        idFuncionario(int): Refere-se ao identificador do funcionário.
        data(str): Refere-se à data que o salário foi pago.
        salario(float): Refere-se ao salário pago para o funcionário.
    '''
    historicoSalarial.append({'idSalarial':idSalarial,
                              'idFuncionario':idFuncionario,
                              'data':data,
                              'salario':salario})
    
def addDependente(idDependente, idFuncionario, parentesco, nome, idade, genero):
    '''
    Esta função adiciona dados de um dependente para a lista `dependentes`.
    
    Args:
        idDependente(int): Refere-se ao identificador do dependente.
        idFuncionario(int): Refere-se ao identificador do funcionário.
        parentesco(str): Refere-se ao parentesco.
        nome(str): Refere-se ao nome do dependente.
        idade(str): Refere-se à data de nascimento do dependente.
        genero(str): Refere-se ao genero do dependente.
    '''
    dependentes.append({'idDependente':idDependente,
                        'idFuncionario':idFuncionario,
                        'parentesco':parentesco,
                        'nome':nome,
                        'idade':idade,
                        'genero':genero})
    
# addFuncionario(idFuncionario, nomeFuncionario, idCargo, idDepartamento, salarioReal, dataNascimento)
addFuncionario(len(funcionarios)+1, 'André Xavier', 4, 1, f'{23:.3f}', '1994-03-17')
addFuncionario(len(funcionarios)+1, 'Andressa Oliveira', 2, 1, f'{4.2:.3f}', '2005-06-23')
addFuncionario(len(funcionarios)+1, 'Roberto Andrade', 1, 1, f'{11:.3f}', '2005-08-05')
addFuncionario(len(funcionarios)+1, 'Laís Gomes', 12, 2, f'{6:.3f}', '2001-06-18')
addFuncionario(len(funcionarios)+1, 'Paula Barbosa Queiroz', 12, 2, f'{9.7:.3f}', '1998-03-12')
addFuncionario(len(funcionarios)+1, 'Mateus Schmidt', 12, 2, f'{9:.3f}', '2002-02-11')
addFuncionario(len(funcionarios)+1, 'Lauro Alvares', 8, 3, f'{5.3:.3f}', '2000-01-27')
addFuncionario(len(funcionarios)+1, 'Edgar Augusto', 9, 3, f'{12:.3f}', '2003-09-30')
addFuncionario(len(funcionarios)+1, 'Amanda Rosa', 10, 4, f'{5.8:.3f}', '1998-03-12')
addFuncionario(len(funcionarios)+1, 'Mario Silva Moreira', 11, 4, f'{9:.3f}', '1985-07-10')
addFuncionario(len(funcionarios)+1, 'Gabriela Alencar', 5, 5, f'{3:.3f}', '2006-05-15')
addFuncionario(len(funcionarios)+1, 'Alessandro Araújo', 6, 5, f'{8.6:.3f}', '1975-07-21')
addFuncionario(len(funcionarios)+1, 'Mara Sousa', 8, 3, f'{5.1:.3f}', '1999-06-22')
addFuncionario(len(funcionarios)+1, 'Alan Silva', 12, 4, f'{5.6:.3f}', '2004-02-18')
addFuncionario(len(funcionarios)+1, 'Daniel Carmo Almeida', 3, 1, f'{20:.3f}', '1973-03-15')
addFuncionario(len(funcionarios)+1, 'Jéssica Borges', 7, 1, f'{20:.3f}', '1993-11-13')
addFuncionario(len(funcionarios)+1, 'Antônio Ferraz', 5, 5, f'{3.3:.3f}', '1999-07-25')
addFuncionario(len(funcionarios)+1, 'Priscila Barreto', 5, 5, f'{3.4:.3f}', '2002-03-11')
addFuncionario(len(funcionarios)+1, 'Paloma Lopez', 5, 5, f'{3.3:.3f}', '2002-11-15')
addFuncionario(len(funcionarios)+1, 'Eduardo Lima', 5, 2, f'{4.8:.3f}', '2001-10-06')
addFuncionario(len(funcionarios)+1, 'Josué Ribeiro', 6, 2, f'{5:.3f}', '1989-12-29')

# addCargo(idCargo, nomeCargo, salarioBase, nivelCargo, escala)
addCargo(len(cargos)+1, 'Desenvolvedor Back-end', f'{9:.3f}', 'Analista', '5x2')
addCargo(len(cargos)+1, 'Desenvolvedor Front-end', f'{4:.3f}', 'Estagiário', '5x2')
addCargo(len(cargos)+1, 'Desenvolvedor Fullstack', f'{18:.3f}', 'Diretor', '4x3')
addCargo(len(cargos)+1, 'Tech Lead', f'{20:.3f}', 'Gerente', '4x3')
addCargo(len(cargos)+1, 'Atendimento ao Cliente', f'{3:.3f}', 'Estagiário', '6x1')
addCargo(len(cargos)+1, 'Representante de Atendimento', f'{8:.3f}', 'Gerente', '5x2')
addCargo(len(cargos)+1, 'CEO', f'{28:.3f}', 'Diretor', '5x2')
addCargo(len(cargos)+1, 'Contador', f'{5:.3f}', 'Analista', '5x2')
addCargo(len(cargos)+1, 'Contador', f'{10:.3f}', 'Gerente', '4x3')
addCargo(len(cargos)+1, 'Recrutador', f'{5:.3f}', 'Analista', '6x1')
addCargo(len(cargos)+1, 'Tech Recruter', f'{8:.3f}', 'Gerente', '5x2')
addCargo(len(cargos)+1, 'Vendedor', f'{5:.3f}', 'Analista', '6x1')
addCargo(len(cargos)+1, 'Marketing Digital', f'{9.:.3f}', 'Gerente', '4x3')

# addDepartamento(idDepartamento, nomeDepartamento, idGerente, andarDepartamento, horarioFuncionamento)
addDepartamento(len(departamentos)+1, 'TI', 1, 3, '8h até 20h')
addDepartamento(len(departamentos)+1, 'Marketing', 12, 4, '8h até 18h')
addDepartamento(len(departamentos)+1, 'Financeiro', 8, 5, '6h até 16h')
addDepartamento(len(departamentos)+1, 'Recursos Humanos', 10, 2, '8h até 18h')
addDepartamento(len(departamentos)+1, 'Suporte ao Cliente', 12, 1, '7h até 23h')

# addHistoricoSalarial(idSalarial, idFuncionario, data, salario)
addHistoricoSalarial(len(historicoSalarial)+1, 1, '2024-09-01', f'{19:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 1, '2024-10-01', f'{19:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 1, '2024-11-01', f'{20:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 1, '2024-12-01', f'{20:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 1, '2025-01-01', f'{23:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 1, '2025-02-01', f'{23:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 2, '2024-09-06', f'{3.8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 2, '2024-10-06', f'{3.8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 2, '2024-11-06', f'{3.8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 2, '2024-12-06', f'{4.2:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 2, '2025-01-06', f'{4.2:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 2, '2025-02-06', f'{4.2:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 3, '2024-09-26', f'{9.7:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 3, '2024-08-26', f'{9.7:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 3, '2024-10-26', f'{10:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 3, '2024-11-26', f'{10:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 3, '2024-12-26', f'{11:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 3, '2025-01-26', f'{11:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 4, '2024-08-20', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 4, '2024-09-20', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 4, '2024-10-20', f'{5.5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 4, '2024-11-20', f'{5.5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 4, '2024-12-20', f'{6:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 4, '2025-01-20', f'{6:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 5, '2024-09-10', f'{9.7:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 5, '2024-10-10', f'{9.7:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 5, '2024-11-10', f'{9.7:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 5, '2024-12-10', f'{9.7:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 5, '2025-01-10', f'{9.7:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 5, '2025-02-10', f'{9.7:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 6, '2024-09-01', f'{9:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 6, '2024-10-01', f'{9:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 6, '2024-11-01', f'{9:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 6, '2024-12-01', f'{9:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 6, '2025-01-01', f'{9:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 6, '2025-02-01', f'{9:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 7, '2024-09-08', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 7, '2024-10-08', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 7, '2024-11-08', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 7, '2024-12-08', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 7, '2025-01-08', f'{5.3:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 7, '2025-02-08', f'{5.3:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 8, '2024-09-06', f'{12:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 8, '2024-10-06', f'{12:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 8, '2024-11-06', f'{12:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 8, '2024-12-06', f'{12:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 8, '2025-01-06', f'{12:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 8, '2025-02-06', f'{12:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 9, '2024-08-26', f'{5.5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 9, '2024-09-26', f'{5.5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 9, '2024-10-26', f'{5.5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 9, '2024-11-26', f'{5.5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 9, '2024-12-26', f'{5.8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 9, '2025-01-26', f'{5.8:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 10, '2024-09-10', f'{9:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 10, '2024-10-10', f'{9:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 10, '2024-11-10', f'{9:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 10, '2024-12-10', f'{9:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 10, '2025-01-10', f'{9:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 10, '2025-02-10', f'{9:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 11, '2024-09-01', f'{3.2:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 11, '2024-10-01', f'{3.2:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 11, '2024-11-01', f'{3.4:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 11, '2024-12-01', f'{3.4:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 11, '2025-01-01', f'{3.4:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 11, '2025-02-01', f'{3.4:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 12, '2024-09-01', f'{8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 12, '2024-10-01', f'{8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 12, '2024-11-01', f'{8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 12, '2024-12-01', f'{8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 12, '2025-01-01', f'{8.6:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 12, '2025-02-01', f'{8.6:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 13, '2024-09-06', f'{4.9:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 13, '2024-10-06', f'{4.9:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 13, '2024-11-06', f'{4.9:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 13, '2024-12-06', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 13, '2025-01-06', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 13, '2025-02-06', f'{5.1:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 14, '2024-09-08', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 14, '2024-10-08', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 14, '2024-11-08', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 14, '2024-12-08', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 14, '2025-01-08', f'{5.6:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 14, '2025-02-08', f'{5.6:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 15, '2024-08-26', f'{19:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 15, '2024-09-26', f'{19:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 15, '2024-10-26', f'{19:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 15, '2024-11-26', f'{19.5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 15, '2024-12-26', f'{19.5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 15, '2025-01-26', f'{20:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 16, '2024-08-20', f'{19.8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 16, '2024-09-20', f'{19.8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 16, '2024-10-20', f'{19.8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 16, '2024-11-20', f'{19.8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 16, '2024-12-20', f'{19.8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 16, '2025-01-20', f'{20:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 17, '2024-09-02', f'{3.3:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 17, '2024-10-02', f'{3.3:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 17, '2024-11-02', f'{3.3:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 17, '2024-12-02', f'{3.3:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 17, '2025-01-02', f'{3.3:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 17, '2025-02-02', f'{3.3:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 18, '2024-09-08', f'{3.2:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 18, '2024-10-08', f'{3.2:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 18, '2024-11-08', f'{3.2:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 18, '2024-12-08', f'{3.2:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 18, '2025-01-08', f'{3.4:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 18, '2025-02-08', f'{3.4:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 19, '2024-09-06', f'{3.3:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 19, '2024-10-06', f'{3.3:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 19, '2024-11-06', f'{3.3:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 19, '2024-12-06', f'{3.3:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 19, '2025-01-06', f'{3.3:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 19, '2025-02-06', f'{3.3:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 20, '2024-09-06', f'{4.8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 20, '2024-10-06', f'{4.8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 20, '2024-11-06', f'{4.8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 20, '2024-12-06', f'{4.8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 20, '2025-01-06', f'{4.8:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 20, '2025-02-06', f'{4.8:.3f}')

addHistoricoSalarial(len(historicoSalarial)+1, 21, '2024-09-06', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 21, '2024-10-06', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 21, '2024-11-06', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 21, '2024-12-06', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 21, '2025-01-06', f'{5:.3f}')
addHistoricoSalarial(len(historicoSalarial)+1, 21, '2025-02-06', f'{5:.3f}')

# addDependente(idDependente, idFuncionario, parentesco, nome, idade, genero)
addDependente(len(dependentes)+1, 1, 'Filho', 'Izaac Xavier', '2010-04-14', 'Masculino')
addDependente(len(dependentes)+1, 1, 'Cônjuge', 'Manuela Silva Xavier', '1996-06-28', 'Feminino')

addDependente(len(dependentes)+1, 2, 'Mãe', 'Laura Pereira Oliveira', '1979-03-25', 'Feminino')
addDependente(len(dependentes)+1, 2, 'Pai', 'Sebastião Oliveira', '1976-06-21', 'Masculino')
addDependente(len(dependentes)+1, 2, 'Filho', 'Juliana Oliveira Soares', '2022-08-15', 'Feminino')

addDependente(len(dependentes)+1, 3, 'Cônjuge', 'Débora Souza Andrade', '2010-07-14', 'Feminino')
addDependente(len(dependentes)+1, 3, 'Mãe', 'Amanda Oliveira Andrade', '1974-06-23', 'Feminino')

addDependente(len(dependentes)+1, 4, 'Pai', 'Anderson Gomes', '1972-01-27', 'Masculino')
addDependente(len(dependentes)+1, 4, 'Irmão', 'Gabriela Gomes', '2007-03-17', 'Feminino')

addDependente(len(dependentes)+1, 5, 'Cônjuge', 'Paulo da Silva Queiroz', '1997-05-24', 'Masculino')
addDependente(len(dependentes)+1, 5, 'Filho', 'Ivana Barbosa Queiroz', '2015-04-15', 'Feminino')

addDependente(len(dependentes)+1, 6, 'Mãe', 'Manuela Schmidt', '1976-09-29', 'Feminino')
addDependente(len(dependentes)+1, 6, 'Irmão', 'Mara Schmidt', '2010-12-25', 'Feminino')

addDependente(len(dependentes)+1, 7, 'Filho', 'Júlia Alvares', '2021-03-05', 'Feminino')
addDependente(len(dependentes)+1, 7, 'Filho', 'Larissa Alvares', '2018-11-25', 'Feminino')

addDependente(len(dependentes)+1, 8, 'Cônjuge', 'Luciana Braz Augusto', '2001-10-04', 'Feminino')
addDependente(len(dependentes)+1, 8, 'Filho', 'Carlos Augusto', '2020-02-16', 'Masculino')

addDependente(len(dependentes)+1, 9, 'Filho', 'Fabiana Rosa da Silva', '2015-08-19', 'Feminino')
addDependente(len(dependentes)+1, 9, 'Filho', 'Edgar Rosa da Silva', '2010-02-21', 'Masculino')

addDependente(len(dependentes)+1, 10, 'Cônjuge', 'Larissa Borbon Moreira', '1986-04-13', 'Feminino')
addDependente(len(dependentes)+1, 10, 'Filho', 'Wagner Moreira', '2007-09-19', 'Masculino')

addDependente(len(dependentes)+1, 11, 'Mãe', 'Sandra Albuquerque Alencar', '1979-12-05', 'Feminino')
addDependente(len(dependentes)+1, 11, 'Pai', 'Leandro Santos Alencar', '1975-11-22', 'Masculino')

addDependente(len(dependentes)+1, 12, 'Cônjuge', 'Patrícia dos Anjos Araújo', '1972-06-07', 'Feminino')
addDependente(len(dependentes)+1, 12, 'Filho', 'Thaísa dos Anjos Araújo', '1998-01-20', 'Feminino')

addDependente(len(dependentes)+1, 13, 'Cônjuge', 'Marcos Ferreira Sousa', '1999-01-22', 'Masculino')
addDependente(len(dependentes)+1, 13, 'Filho', 'Lucas Sousa', '2020-01-14', 'Masculino')

addDependente(len(dependentes)+1, 14, 'Mãe', 'Maria Soares Silva', '2011-01-14', 'Feminino')
addDependente(len(dependentes)+1, 14, 'Filho', 'Daniela Silva', '2024-01-01', 'Feminino')

addDependente(len(dependentes)+1, 15, 'Cônjuge', 'Carla Gross Almeida', '1984-02-03', 'Feminino')
addDependente(len(dependentes)+1, 15, 'Filho', 'Roberta Landini Almeida', '2007-05-05', 'Feminino')
addDependente(len(dependentes)+1, 15, 'Filho', 'Luana Gross Almeida', '1997-07-07', 'Feminino')

addDependente(len(dependentes)+1, 16, 'Cônjuge', 'Anderson Gonçalves Borges', '1998-01-25', 'Masculino')
addDependente(len(dependentes)+1, 16, 'Filho', 'Tainara Borges', '2018-07-08', 'Feminino')

addDependente(len(dependentes)+1, 17, 'Cônjuge', 'Andressa Almeida Ferraz', '1998-09-09', 'Feminino')
addDependente(len(dependentes)+1, 17, 'Filho', 'Fábia Almeida Ferraz', '2016-10-12', 'Feminino')

addDependente(len(dependentes)+1, 18, 'Mãe', 'Ana Alves de Souza', '1972-04-05', 'Feminino')
addDependente(len(dependentes)+1, 18, 'Pai', 'André Barreto', '1972-03-26', 'Masculino')

addDependente(len(dependentes)+1, 19, 'Pai', 'Alexandre da Silva Lopez', '1970-12-12', 'Masculino')
addDependente(len(dependentes)+1, 19, 'Irmão', 'Alberto Lopez', '2018-05-14', 'Masculino')

addDependente(len(dependentes)+1, 20, 'Cônjuge', 'Leila Boaventura Lima', '2010-08-07', 'Feminino')
addDependente(len(dependentes)+1, 20, 'Filho', 'Fabrício Lima', '2023-01-13', 'Masculino')

addDependente(len(dependentes)+1, 21, 'Cônjuge', 'Alessandra Lopez Ribeiro', '1994-09-18', 'Feminino')
addDependente(len(dependentes)+1, 21, 'Filho', 'Caio Ribeiro', '2014-08-21', 'Masculino')


def inserirDadosCsv(nomeArquivo, lista, *campos):
    '''
    Esta função cria um arquivo .CSV personalizado como base no nome do arquivo, lista e os campos.
    
    Args:
        nomeArquivo(str): Refere-se ao nome do arquivo que irá ser gerado.
        lista(list[obj]): Refere-se à uma lista de dados criada nas funções anteriores.
        campos(*Args): Refere-se aos campos que a tabela .CSV terá.
    '''
    with open(f'tabelas/tb_{nomeArquivo}.csv', mode='w', newline='', encoding='utf-8') as csvfile:
        digitador = csv.DictWriter(csvfile, fieldnames=[campo for campo in campos])
        digitador.writeheader()
        for dado in lista:
            digitador.writerow(dado)
    print(f'{nomeArquivo.title()}s adicionados com sucesso!')  
          
# inserirDadosCsv(nomeArquivo, lista, *campos)
inserirDadosCsv('funcionario', funcionarios, 'idFuncionario', 'nomeFuncionario', 'idCargo', 'idDepartamento', 'salarioReal', 'dataNascimento')
inserirDadosCsv('cargo', cargos, 'idCargo', 'nomeCargo', 'salarioBase', 'nivelCargo', 'escala')    
inserirDadosCsv('departamento', departamentos, 'idDepartamento', 'nomeDepartamento', 'idGerente', 'andarDepartamento', 'horarioFuncionamento')      
inserirDadosCsv('historicoSalarial', historicoSalarial, 'idSalarial', 'idFuncionario', 'data', 'salario')        
inserirDadosCsv('dependente', dependentes, 'idDependente', 'idFuncionario', 'parentesco', 'nome', 'idade', 'genero') 
            