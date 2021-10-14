import pyodbc
import datetime

class GEMPRE_CERTIFICADOS:
    banco = pyodbc.connect('DSN=Contabil')
    cursor = banco.cursor()

    cursor.execute(
        f"SELECT codi_emp, razao_emp, cgce_emp, stat_emp FROM externo.bethadba.geempre"
    )
    info_emp = cursor.fetchall()

    cursor.execute(
        f"SELECT CODI_EMP, TIPO, VALIDADE_FIM FROM externo.bethadba.GECERTIFICADOSDIGITAIS"
    )
    certificado_emp = cursor.fetchall()

    lista_emp_certificado = None

    def certificado_empresas(self):
        self.lista_emp_certificado = []
        for empresa in self.info_emp:
            codigo_empresa = empresa[0]
            razao_empresa = empresa[1]
            cnpj_empresa = empresa[2]
            cnpj = f"{cnpj_empresa[:2]}.{cnpj_empresa[2:5]}.{cnpj_empresa[5:8]}/{cnpj_empresa[8:12]}-{cnpj_empresa[12:]}"
            status_emp = empresa[3]

            if status_emp == 'A':

                for certificado in self.certificado_emp:
                    codi_emp = certificado[0]
                    tipo_certificado = certificado[1]
                    validade_certificado = certificado[2]
                    data_fim = f"{validade_certificado:%d/%m/%Y}"

                    if codigo_empresa == codi_emp:
                        status_certificado = self.verificar_status(validade_certificado)
                        self.lista_emp_certificado.append((codigo_empresa, razao_empresa, cnpj, tipo_certificado,
                                                          data_fim, status_certificado))

        return self.lista_emp_certificado

    @staticmethod
    def verificar_status(date_vencimento):
        date_today = datetime.date.today()

        dif_date = (date_vencimento - date_today).days

        if dif_date <= 0:
            stats_date = "Vencido"
        elif dif_date <= 30:
            stats_date = "À Vencer"
        else:
            stats_date = "Válido"

        return stats_date
