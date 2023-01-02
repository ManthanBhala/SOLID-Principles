class Invoice:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price
    
    def getTotal(self):
        pass


class InvoiceDB:
    def __init__(self, invoice):
        self.invoice = invoice
    
    def saveInvoice(self):
        pass


class InvoicePrinter:
    def __init__(self, invoice):
        self.invoice = invoice
    
    def printInvoice(self):
        pass
