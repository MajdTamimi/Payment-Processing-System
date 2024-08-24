class CurrencyConverter:
    def __init__(self, rates: dict):
        self.rates = rates

    def convert(self, amount: float, from_currency: str, to_currency: str) -> float:
        if from_currency == to_currency:
            return amount
        rate = self.rates.get((from_currency, to_currency))
        if rate:
            return amount * rate
        raise ValueError("Conversion rate not available.")