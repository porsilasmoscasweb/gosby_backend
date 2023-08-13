from classes.master import Master


class Transaction(Master):

    transactions = [
        {"sku": "T2006", "amount": "10.00", "currency": "USD"},
        {"sku": "M2007", "amount": "34.57", "currency": "CAD"},
        {"sku": "R2008", "amount": "17.95", "currency": "USD"},
        {"sku": "T2006", "amount": "7.63", "currency": "EUR"},
        {"sku": "B2009", "amount": "21.23", "currency": "USD"}
    ]

    all = []

    def __init___(self, sku, amount, currency):
        self.sku = sku
        self.amount = amount
        self.currency = currency

    def getAll():
        return Transaction.transactions

    def getAllAttr(attr, value):
        return Transaction.findOnObj(Transaction.transactions, attr, value, True)
