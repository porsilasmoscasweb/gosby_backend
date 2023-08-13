from classes.master import Master


class CurrencyRates(Master):

    currencyRates = [
        {"from": "EUR", "to": "USD", "rate": "1.359"},
        {"from": "CAD", "to": "EUR", "rate": "0.732"},
        {"from": "USD", "to": "EUR", "rate": "0.736"},
        {"from": "EUR", "to": "CAD", "rate": "1.366"}
    ]

    def __init___(self, _from, to, rate):
        self._from = _from
        self.to = to
        self.rate = rate

    def getAll():
        return CurrencyRates.currencyRates

    def getAttr(attr, value):
        return CurrencyRates.findOnObj(CurrencyRates.currencyRates, [attr], [value], False)
