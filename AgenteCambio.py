import requests

class AgenteCambio:
    def __init__(self, moeda_origem, moeda_destino, quantidade):
        self.moeda_origem = moeda_origem
        self.moeda_destino = moeda_destino
        self.quantidade = quantidade

    def taxa_de_cambio(self):
        url = 'https://api.exchangerate-api.com/v4/latest/{0}'.format(self.moeda_origem)
        response = requests.get(url)
        data = response.json()
        taxa_cambio = data['rates'][self.moeda_destino]
        return taxa_cambio

    def converter(self):
        taxa_cambio = self.taxa_de_cambio()
        resultado = self.quantidade * taxa_cambio
        return resultado
