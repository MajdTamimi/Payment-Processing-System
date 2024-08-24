import unittest
from src.currency_converter import CurrencyConverter

class TestCurrencyConverter(unittest.TestCase):
    
    def test_convert_currency(self):
        converter = CurrencyConverter()
        rate = 1.2  # Assume 1 USD = 1.2 EUR
        self.assertEqual(converter.convert(100, rate), 120)  # 100 USD should be 120 EUR

if __name__ == '__main__':
    unittest.main()
