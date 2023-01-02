class ProductInterface:
    def addItems(self, quantity, price):
        pass


class Product(ProductInterface):
    def addItems(self, quantity, price):
        pass


class PaymentInterface:
    def processPayment(self, amount):
        pass


class Payment(PaymentInterface):
    def processPayment(self, amount):
        pass