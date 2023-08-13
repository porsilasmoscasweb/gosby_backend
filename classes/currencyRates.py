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

    def convertCurrency(curr_from, to):
        convertRate = CurrencyRates.findOnObj(CurrencyRates.currencyRates, [
            'from', 'to'], [curr_from, to], False)

        # If the result not exists. Try to get the first from 'FROM'
        if len(convertRate) == 0:
            convertRate = CurrencyRates.findOnObj(CurrencyRates.currencyRates, [
                'from'], [curr_from], False)

        # If this also not exists return false
        if len(convertRate) == 0:
            return False

        # If exists get the first of new value 'TO' from the 'TO' passed as a param
        convertRate = CurrencyRates.findOnObj(CurrencyRates.currencyRates, [
            'to'], [to], False)

        # If this also not exists return false
        if len(convertRate) == 0:
            return False

        return convertRate.get('rate')
