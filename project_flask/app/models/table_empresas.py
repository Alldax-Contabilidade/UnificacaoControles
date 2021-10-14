import pandas as pd


class Empresa:
    df = pd.read_excel(r'C:\Users\matheus.oliveira\Documents\Repository\ControleClientes\project_flask\app\static\plan'
                       r'\empresas.xlsx')

    def colunas(self):
        colunas = self.df.columns

        return colunas

    def itens(self):
        return self.df.iterrows()


# emp = Empresa()
# emp.colunas()
# emp.itens()