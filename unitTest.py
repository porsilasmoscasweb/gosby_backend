import unittest


class TestMethod(unittest.TestCase):

    def test_allCurrencyRates(self):
        self.assertEqual(len(currencyRates), 4, "Should be 4")


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

    unittest.main()
