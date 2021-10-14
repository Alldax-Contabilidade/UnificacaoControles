from app import app
from flask import render_template, request
from ..models.dados_dominio_empresas import GEEMPRE
from ..models.dados_dominio_funcionarios import CFUNCIONARIOS
from ..models.dados_dominio_certificado import GEMPRE_CERTIFICADOS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/empresas')
def empresas():
    emp = GEEMPRE()
    info = emp.cadastro_empresas()
    return render_template('pag_empresas.html', rows=info)


@app.route('/empresas/<cod_emp>')
def info_empresa(cod_emp):

    reg_fed_key = {1: "Lucro Real", 5: "Lucro Presumido", 6: "Regime Especial Trib.",
                   8: "Imune IRPJ", 9: "Isenta IRPJ"}

    global dina_emp, razao_emp, cnpj, stat_emp, data_ini, regime_tributario, ramo_emp, ucta, uefi, ufol
    emp = GEEMPRE()
    dados = emp.informacoes_cliente(cod_emp)
    for razao_emp, cnpj_emp, stat_emp, data_inicio, data_fim, ramo_emp, ucta, uefi, ufol in dados:
        cnpj = f"{cnpj_emp[:2]}.{cnpj_emp[2:5]}.{cnpj_emp[5:8]}/{cnpj_emp[8:12]}-{cnpj_emp[12:]}"
        data_ini = f"{data_inicio:%d/%m/%Y}"
        if data_fim is None:
            dina_emp = ""
        else:
            dina_emp = f"{data_fim:%d/%m/%Y}"

    simplsn, reg_fed = emp.parametro_fiscal(cod_emp)
    if simplsn == 'S':
        regime_tributario = "Simples Nacional"
    else:
        if reg_fed in reg_fed_key:
            regime_tributario = reg_fed_key[reg_fed]

    return render_template('pag-ind-emp.html', cod_emp=cod_emp, nome_emp=razao_emp, cnpj_emp=cnpj,
                           status=stat_emp, ini_date=data_ini, fim_date=dina_emp, regi_trib=regime_tributario,
                           ramo_atv=ramo_emp, contabil=ucta, fiscal=uefi, folha=ufol)


# @app.route('/departamentos')
# def departamentos():
#
#     func = CFUNCIONARIOS()
#     func.cadastro_funcionario()
#     admin, autom, consult, contab, control, financ, fiscal, pessoal, recur_hum, relacion, societ = func.funcionarios_departamentos()
#
#     return render_template('pag-departamentos.html', administrativo=admin, automacao=autom, consultoria=consult,
#                            contabil=contab, controladoria=control, financeiro=financ, fiscal=fiscal, pessoal=pessoal,
#                            rh=recur_hum, relacionamento=relacion, societario=societ)


@app.route('/certificado')
def certificado():
    certificados = GEMPRE_CERTIFICADOS()
    info_certificados = certificados.certificado_empresas()
    return render_template('pag_certificados.html', lista=info_certificados)


@app.route('/departamentos')
def atividades():
    return render_template('pag_atividades.html')


@app.route('/departamentos/<dpto>', methods=["GET", "POST"])
def ativ_dpto(dpto):

    if request.method == "POST":
        competencia = request.form['select-competencia']
        print(competencia)

    return render_template("pag_atv_dpto.html", title=dpto)
