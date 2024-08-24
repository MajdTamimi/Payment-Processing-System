import unittest
from src.payment_methods import CreditCardPayment, PayPalPayment, CryptoPayment

class TestPaymentMethods(unittest.TestCase):

    def test_credit_card_payment(self):
        payment_method = CreditCardPayment()
        payment_method.validate()
        payment_method.process_payment(100.0)

    def test_paypal_payment(self):
        payment_method = PayPalPayment()
        payment_method.validate()
        payment_method.process_payment(150.0)

    def test_crypto_payment(self):
        payment_method = CryptoPayment()
        payment_method.validate()
        payment_method.process_payment(200.0)

if __name__ == '__main__':
    unittest.main()