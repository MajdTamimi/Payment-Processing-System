from payment_methods import IPaymentMethod, CreditCardPayment, PayPalPayment, CryptoPayment

class PaymentProcessor:
    def __init__(self, payment_method: IPaymentMethod):
        self.payment_method = payment_method

    def process(self, amount: float):
        self.payment_method.validate()
        self.payment_method.process_payment(amount)

# Example usage
if __name__ == "__main__":
    payment_method = CreditCardPayment()
    processor = PaymentProcessor(payment_method)
    processor.process(100.0)