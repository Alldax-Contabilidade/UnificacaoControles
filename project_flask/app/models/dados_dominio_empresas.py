import pyodbc
import datetime


class GEEMPRE:
    banco = pyodbc.connect('DSN=Contabil')
    cursor = banco.cursor()

    def cadastro_empresas(self):
        self.cursor.execute("SELECT codi_emp, nome_emp, cgce_emp, stat_emp FROM externo.bethadba.geempre")
        cadastros = self.cursor.fetchall()

        return cadastros

    def informacoes_cliente(self, codi_emp):
        self.cursor.execute(f"SELECT razao_emp, cgce_emp, stat_emp, dcad_emp, dina_emp, "
                            f"ramo_emp, ucta_emp, uefi_emp, ufol_emp "
                            f"FROM externo.bethadba.geempre "
                            f"WHERE codi_emp = {codi_emp}")
        dados_emp = self.cursor.fetchall()

        return dados_emp

    def parametro_fiscal(self, CODI_EMP):
        qnt_dias = []

        self.cursor.execute(
            f"SELECT VIGENCIA_PAR FROM externo.bethadba.EFPARAMETRO_VIGENCIA WHERE CODI_EMP = {CODI_EMP}"
        )

        datas_par = self.cursor.fetchall()
        today = datetime.date.today()

        for data in datas_par:

            dif_date = abs((today - data[0]).days)
            qnt_dias.append(dif_date)

        vlr_min = min(qnt_dias)
        idx = qnt_dias.index(vlr_min)
        data_par = f"{datas_par[idx][0]:%Y%m%d}"

        self.cursor.execute(
            f"SELECT SIMPLESN_OPTANTE_PAR, RFED_PAR FROM externo.bethadba.EFPARAMETRO_VIGENCIA"
            f" WHERE CODI_EMP = {CODI_EMP} AND VIGENCIA_PAR = {data_par}"
        )
        dados_regime = self.cursor.fetchall()
        SN, RFED = dados_regime[0]

        return SN, RFED
