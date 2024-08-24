import unittest
import os
from src.transaction_logger import TransactionLogger

class TestTransactionLogger(unittest.TestCase):
    
    def setUp(self):
        self.logger = TransactionLogger('test_transactions.log')

    def tearDown(self):
        if os.path.exists('test_transactions.log'):
            os.remove('test_transactions.log')

    def test_log_transaction(self):
        self.logger.log_transaction("CreditCard", 100, "2024-08-24 10:00:00", "Success")
        with open('test_transactions.log', 'r') as file:
            content = file.read()
            self.assertIn("CreditCard", content)
            self.assertIn("100", content)
            self.assertIn("Success", content)

if __name__ == '__main__':
    unittest.main()
