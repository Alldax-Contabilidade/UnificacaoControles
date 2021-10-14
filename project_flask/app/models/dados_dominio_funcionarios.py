import pyodbc


class CFUNCIONARIOS:
    banco = pyodbc.connect('DSN=Contabil')
    cursor = banco.cursor()

    dados_funcionarios = None

    administrativo = None
    automacao = None
    consultoria = None
    contabil = None
    controladoria = None
    financeiro = None
    fiscal = None
    pessoal = None
    recursos_humanos = None
    societario = None
    relacionamento = None

    lista_funcionarios = []

    def cadastro_funcionario(self):
        self.cursor.execute(
            f"SELECT codi_emp, i_empregados, nome, admissao, i_depto FROM externo.bethadba.foempregados WHERE codi_emp IN (249, 301)"
        )
        self.dados_funcionarios = self.cursor.fetchall()

        self.cursor.execute(
            f"SELECT codi_emp, i_empregados FROM externo.bethadba.forescisoes WHERE codi_emp IN (249, 301)"
        )
        dados_rescicoes = self.cursor.fetchall()

        for cod in dados_rescicoes:

            for funcionario in self.dados_funcionarios:
                if cod[0] == funcionario[0] and cod[1] == funcionario[1]:

                    self.dados_funcionarios.remove(funcionario)

                else:
                    pass

    def funcionarios_departamentos(self):
        self.administrativo = []
        self.automacao = []
        self.consultoria = []
        self.contabil = []
        self.controladoria = []
        self.financeiro = []
        self.fiscal = []
        self.pessoal = []
        self.recursos_humanos = []
        self.societario = []
        self.relacionamento = []

        for funcionario in self.dados_funcionarios:
            codi_emp = funcionario[0]
            codi_dpto = funcionario[4]

            if codi_emp == 301 and codi_dpto == 9 or codi_emp == 249 and codi_dpto == 14:
                self.contabil.append(funcionario)

            elif codi_emp == 301 and codi_dpto == 7 or codi_emp == 249 and codi_dpto == 13 or \
                 codi_emp == 249 and codi_dpto == 22:  # fiscal
                self.fiscal.append(funcionario)

            elif codi_emp == 301 and codi_dpto == 8 or codi_emp == 249 and codi_dpto == 15:  # pessoal
                self.pessoal.append(funcionario)

            elif codi_emp == 301 and codi_dpto == 11 or codi_emp == 249 and codi_dpto == 12:  # societario
                self.societario.append(funcionario)

            elif codi_emp == 249 and codi_dpto == 11:
                self.administrativo.append(funcionario)

            elif codi_emp == 249 and codi_dpto == 23:
                self.automacao.append(funcionario)

            elif codi_emp == 249 and codi_dpto == 24:
                self.consultoria.append(funcionario)

            elif codi_emp == 249 and codi_dpto == 17:
                self.controladoria.append(funcionario)

            elif codi_emp == 249 and codi_dpto == 20:  # financeiro
                self.financeiro.append(funcionario)

            elif codi_emp == 249 and codi_dpto == 16:  # recursos_humanos
                self.recursos_humanos.append(funcionario)

            elif codi_emp == 249 and codi_dpto == 21: # relacionamento
                self.relacionamento.append(funcionario)

        return self.administrativo, self.automacao, self.consultoria, self.contabil, self.controladoria, \
               self.financeiro, self.fiscal, self.pessoal, self.recursos_humanos, self.relacionamento, self.societario


# func = CFUNCIONARIOS()
# func.cadastro_funcionario()
# func.separar_departamentos()
