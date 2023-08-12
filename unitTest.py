import unittest


class TestMethod(unittest.TestCase):

    def test_allCurrencyRates(self):
        self.assertEqual(len(currencyRates), 4, "Should be 4.")

    def test_singleCurrencyRates(self):
        currency = findOnObj(currencyRates, 'from', 'EUR', False)

        self.assertEqual(len(currency), 3, "Should be 3.")

    def test_allTransactionsByCode(self):
        trans = findOnObj(transactions, 'currency', 'USD', True)

        self.assertEqual(len(trans), 3, "Should be 3.")


if __name__ == '__main__':
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

    unittest.main()
