class DiscountStrategy:
    def getDiscount(self):
        pass


class HDFCDiscountStrategy(DiscountStrategy):
    def getDiscount(self):
        print("5 percent discount")
    
    def checkAvailableCards(self):
        print("Regalia")
        print("Diners Black")