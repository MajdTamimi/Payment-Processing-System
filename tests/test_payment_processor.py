import unittest
from src.payment_processor import PaymentProcessor
from src.payment_methods import CreditCardPayment, PayPalPayment, CryptoPayment

class TestPaymentProcessor(unittest.TestCase):

    def test_process_credit_card(self):
        processor = PaymentProcessor(CreditCardPayment())
        processor.process(100.0)

    def test_process_paypal(self):
        processor = PaymentProcessor(PayPalPayment())
        processor.process(150.0)

    def test_process_crypto(self):
        processor = PaymentProcessor(CryptoPayment())
        processor.process(200.0)

if __name__ == '__main__':
    unittest.main()
