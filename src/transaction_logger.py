import logging

class TransactionLogger:
    def __init__(self, log_file: str = "transactions.log"):
        logging.basicConfig(filename=log_file, level=logging.INFO)

    def log_transaction(self, method: str, amount: float, success: bool):
        logging.info(f"Method: {method}, Amount: ${amount}, Success: {success}")
