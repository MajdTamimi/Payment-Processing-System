from abc import ABC, abstractmethod

class IPaymentMethod(ABC):
    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def process_payment(self, amount: float):
        pass

class CreditCardPayment(IPaymentMethod):
    def validate(self):
        print("Validating Credit Card details...")

    def process_payment(self, amount: float):
        print(f"Processing Credit Card payment of ${amount}")

class PayPalPayment(IPaymentMethod):
    def validate(self):
        print("Validating PayPal details...")

    def process_payment(self, amount: float):
        print(f"Processing PayPal payment of ${amount}")

class CryptoPayment(IPaymentMethod):
    def validate(self):
        print("Validating Cryptocurrency details...")

    def process_payment(self, amount: float):
        print(f"Processing Cryptocurrency payment of ${amount}")
