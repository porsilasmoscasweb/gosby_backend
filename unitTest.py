import unittest

from classes.currencyRates import CurrencyRates
from classes.transaction import Transaction


class TestMethod(unittest.TestCase):

    def test_allCurrencyRates(self):
        self.assertEqual(len(CurrencyRates.getAll()), 4, "Should be 4.")

    def test_singleCurrencyRates(self):
        self.assertEqual(len(CurrencyRates.getAttr(
            'from', 'EUR')), 3, "Should be 3.")

    def test_singleCurrencyRatesType(self):
        self.assertEqual(type(CurrencyRates.getAttr(
            'from', 'USD')), dict, "Should be Dictionary.")

    def test_allTransactionsByCode(self):
        self.assertEqual(len(Transaction.getAllAttr(
            ['currency'], ['USD'])), 3, "Should be 3.")

    def test_allTransactionsByCodeAnSku(self):
        self.assertEqual(len(Transaction.getAllAttr(
            ['currency', 'sku'], [
                'USD', 'R2008'])), 1, "Should be 1.")


if __name__ == '__main__':
    unittest.main()
