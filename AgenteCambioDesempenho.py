import requests
import datetime

class AgenteCambioDesempenho:
    def __init__(self, moeda_origem, moeda_destino, quantidade, data_inicio, data_fim):
        self.moeda_origem = moeda_origem
        self.moeda_destino = moeda_destino
        self.quantidade = quantidade
        self.data_inicio = datetime.datetime.strptime(data_inicio, '%Y-%m-%d').date()
        self.data_fim = datetime.datetime.strptime(data_fim, '%Y-%m-%d').date()

    def taxa_de_cambio(self, data):
        url = f'https://api.exchangerate-api.com/v4/{data.strftime("%Y-%m-%d")}/{self.moeda_origem}'
        response = requests.get(url)
        data = response.json()
        taxa_cambio = data['rates'][self.moeda_destino]
        return taxa_cambio

    def converter(self, data):
        taxa_cambio = self.taxa_de_cambio(data)
        resultado = self.quantidade * taxa_cambio
        return resultado

    def calcular_desempenho(self):
        data = self.data_inicio
        resultados = []
        while data <= self.data_fim:
            resultado = self.converter(data)
            resultados.append(resultado)
            data += datetime.timedelta(days=1)

        desempenho = ((resultados[-1] - resultados[0]) / resultados[0]) * 100
        return desempenho
