class Investidor:
    def __init__(self, nome, saldo_inicial):
        self.nome = nome
        self.saldo = saldo_inicial
        self.portfolio = {}

    def comprar_ativo(self, ativo, quantidade, preco_unitario):
        custo = quantidade * preco_unitario
        if custo > self.saldo:
            raise ValueError('Saldo insuficiente para comprar este ativo.')
        else:
            if ativo in self.portfolio:
                self.portfolio[ativo] += quantidade
            else:
                self.portfolio[ativo] = quantidade
            self.saldo -= custo

    def vender_ativo(self, ativo, quantidade, preco_unitario):
        if ativo not in self.portfolio:
            raise ValueError('Este ativo não está presente no portfolio.')
        elif quantidade > self.portfolio[ativo]:
            raise ValueError('Quantidade insuficiente deste ativo no portfolio.')
        else:
            receita = quantidade * preco_unitario
            self.portfolio[ativo] -= quantidade
            self.saldo += receita

    def valor_portfolio(self, preco_ativos):
        valor = self.saldo
        for ativo, quantidade in self.portfolio.items():
            valor += quantidade * preco_ativos[ativo]
        return valor
