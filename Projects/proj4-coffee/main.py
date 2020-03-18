class CashBox:
    # where are we accepting these coins from?
    def __init__(self, credit, totalReceived): #probably not the right inputs. :P
        self.credit = credit                #int
        self.totalReceived = totalReceived  #int

        self.julieTotal = 0

    def deposit(self, amount):
        self.julieTotal += amount

    def returnCoins(self):
        pass

    def haveYou(self, amount):
        # return amount > self.julieTotal
        pass

    def deduct(self, amount):
        self.julieTotal -= amount

    def total(self):
        return self.julieTotal


class Product:
    def __init__(self, name, price, recipe):
        self.name = name      #string
        self.price = price    #int
        self.recipe = recipe  #list of strings

    def getPrice(self):
        return self.price

    def make(self):
        pass
        # return self.recipe

class Selector(CashBox):
    def __init__(self, credit, totalReceived, products):
        self.cashBox = CashBox.__init__(self, credit, totalReceived)
        self.products = products



class CoffeeMachine(CashBox, Selector):
    def __init__(self):
        self.cashBox = CashBox.__init__(self)
        self.selector = Selector.__init__(self, self.cashBox)

    def oneAction(self, input):
        if input == 'quit':
            return False
        return True

    def totalCash(self):
        return self.cashBox.total()


def main():
    m = CoffeeMachine()
    while m.oneAction():
        pass
    total = m.totalCash()
    print(f"Total cash ${total/100:.2f}")