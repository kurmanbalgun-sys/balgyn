# task5_payment_system.py
from abc import ABC, abstractmethod

class PaymentSystem(ABC):

    @abstractmethod
    def authorize(self, amount):
        pass

    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CreditCardPayment(PaymentSystem):
    def authorize(self, amount):
        return f"Кредитная карта: сумма {amount} успешно авторизована."

    def process_payment(self, amount):
        return f"Кредитная карта: платёж на {amount} выполнен."

    def refund(self, amount):
        return f"Кредитная карта: возврат {amount} выполнен."


class PayPalPayment(PaymentSystem):
    def authorize(self, amount):
        return f"PayPal: сумма {amount} успешно авторизована."

    def process_payment(self, amount):
        return f"PayPal: платёж на {amount} выполнен."

    def refund(self, amount):
        return f"PayPal: возврат {amount} выполнен."


if __name__ == "__main__":
    cc = CreditCardPayment()
    pp = PayPalPayment()

    print(cc.authorize(100))
    print(cc.process_payment(100))
    print(cc.refund(50))

    print(pp.authorize(200))
    print(pp.process_payment(200))
    print(pp.refund(100))
