from flask import Flask, request
from classes.currencyRates import CurrencyRates
from classes.transaction import Transaction
app = Flask(__name__)


@app.route('/all-currency-rates')
def allCurrencyRates():
    request
    return CurrencyRates.getAll()


@app.route('/currency-rates')
def singleCurrencyRates():
    request
    code = request.args.get('code')

    currency = CurrencyRates.getAttr('from', code)

    return currency


@app.route('/all-transactions')
def allTransactionsByCode():
    request

    attrs = getArrRequestTrans(request, ['currency', 'sku'])

    trans = Transaction.getAllAttr(attrs[0], attrs[1])

    return trans


'''
Get all attributes from request
@return list
'''
def getArrRequestTrans(request, attributes):
    attrs = []
    vals = []

    for attr in attributes:
        value = request.args.get(attr)

        if value is not None:
            attrs.insert(-1, attr)
            vals.insert(-1, value)

    list1 = (attrs, vals)

    return list1


if __name__ == '__main__':
    app.run(debug=True)
