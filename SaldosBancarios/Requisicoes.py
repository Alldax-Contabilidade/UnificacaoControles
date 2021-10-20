import requests
import json

class Query:
    def requsicao_base(self):
        url = "https://app.omie.com.br/api/v1/financas/extrato/"
        headers = {'Content-Type': 'application/json'}
        json = '''{"call":"ListarExtrato","app_key":"1458834874497","app_secret":"50d3875c8e0c43b95e0ee34925fa00a4","param":[{"nCodCC":2147372697,"cCodIntCC":"","dPeriodoInicial":"08/10/2021","dPeriodoFinal":"08/10/2021"}]}'''

        request = requests.post(url= url, data= json, headers= headers)
        print(request.content)

# TESTE
Query().requsicao_base()
