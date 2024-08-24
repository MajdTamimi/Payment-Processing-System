import unittest
from src.discounts import PercentageDiscount, FixedAmountDiscount

class TestDiscounts(unittest.TestCase):
    
    def test_percentage_discount(self):
        discount = PercentageDiscount(10)  # 10% discount
        self.assertEqual(discount.apply_discount(100), 90)  # 10% of 100 is 10, so the result should be 90

    def test_fixed_amount_discount(self):
        discount = FixedAmountDiscount(20)  # $20 discount
        self.assertEqual(discount.apply_discount(100), 80)  # 100 - 20 should be 80

if __name__ == '__main__':
    unittest.main()
