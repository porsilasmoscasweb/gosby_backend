from flask import Flask, request, jsonify
app = Flask(__name__)


transactions = [
    {"sku": "T2006", "amount": "10.00", "currency": "USD"},
    {"sku": "M2007", "amount": "34.57", "currency": "CAD"},
    {"sku": "R2008", "amount": "17.95", "currency": "USD"},
    {"sku": "T2006", "amount": "7.63", "currency": "EUR"},
    {"sku": "B2009", "amount": "21.23", "currency": "USD"}
]

currencyRates = [
    {"from": "EUR", "to": "USD", "rate": "1.359"},
    {"from": "CAD", "to": "EUR", "rate": "0.732"},
    {"from": "USD", "to": "EUR", "rate": "0.736"},
    {"from": "EUR", "to": "CAD", "rate": "1.366"}
]


def findOnObj(arr, search_key, search_value, multiple):
    new_dictionary = []

    for obj in arr:
        if (obj.get(search_key) == search_value):
            if not multiple:
                return obj

            new_dictionary.append(obj)

    return new_dictionary


@app.route('/all-currency-rates')
def allCurrencyRates():
    request
    return currencyRates


@app.route('/currency-rates')
def singleCurrencyRates():

    request
    code = request.args.get('code')
    multiple = False

    currency = findOnObj(currencyRates, 'from', code, multiple)

    return currency


@app.route('/all-transactions')
def allTransactionsByCode():
    request

    code = request.args.get('code')
    multiple = True

    trans = findOnObj(transactions, 'currency', code, multiple)

    return trans


if __name__ == '__main__':
    app.run(debug=True)
