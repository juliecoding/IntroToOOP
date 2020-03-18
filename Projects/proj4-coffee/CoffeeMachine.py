class CoffeeMachine:
    def __init__(self):
        self.cashBox = CashBox()
        self.selector = Selector(self.cashBox)
        self.instructionsAlreadyDisplayed = False

    def oneAction(self):
        if not self.instructionsAlreadyDisplayed:
            self.displayInstructions()
            self.instructionsAlreadyDisplayed = True
        command = input("Your command: ").lower().split()
        mainInstruction = command[0]
        if len(command) > 1:
            amountOrIndex = int(command[1])

        if mainInstruction == 'insert':
            if amountOrIndex not in [5, 10, 25, 50]:
                print("INPUT ERROR >>>")
                print("We only take half-dollars, quarters, dimes, and nickels.")
                self.cashBox.returnCoins()
            else:
                self.cashBox.deposit(amountOrIndex)
        elif mainInstruction == 'select':
            if len(command) < 2 or amountOrIndex > 5 or amountOrIndex < 1:
                print("Please provide the number of the product you wish to select.")
                print("1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon")
            else:
                self.selector.select(amountOrIndex - 1)
        elif mainInstruction == 'cancel':
            self.cashBox.returnCoins(self.cashBox.credit)
        elif mainInstruction == 'quit':
            self.cashBox.returnCoins()
            return
        else:
            print("Invalid command.")
        self.oneAction()

    def displayInstructions(self):
        print("Product List: all 35 cents, except bouillon (25 cents)")
        print("1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon")
        print("Sample commands: insert 25, select 1")

    def totalCash(self):
        return self.cashBox.total()


class CashBox:
    def __init__(self):
        self.credit = 0
        self.totalReceived = 0

    def deposit(self, amount):
        self.credit += amount
        print(f"Depositing {amount} cents. You have {self.credit} cents credit.")
        self.totalReceived += amount

    def returnCoins(self, amount = 0):
        self.totalReceived -= self.credit
        self.credit = 0
        if amount:
            print(f"Returning {amount} cents.")
        else:
            print("Coin(s) returned.")

    def haveYou(self, amount):
        if self.credit >= amount:
            return True
        return False

    def deductFromCredit(self, amount):
        self.credit -= amount

    def total(self):
        return self.totalReceived


class Selector:
    def __init__(self, cashBox):
        self.cashBox = cashBox
        self.products = [
            Product(
                "black",
                35,
                "    Dispensing cup \n    Dispensing coffee \n    Dispensing water"
            ),
            Product(
                "white",
                35,
                "    Dispensing cup \n    Dispensing coffee \n    Dispensing creamer \n    Dispensing water"
            ),
            Product(
                "sweet",
                35,
                "    Dispensing cup \n    Dispensing coffee \n    Dispensing sugar \n    Dispensing water"
            ),
            Product(
                "white & sweet",
                35,
                "    Dispensing cup \n    Dispensing coffee \n    Dispensing sugar \n    Dispensing creamer \n    Dispensing water"
            ),
            Product(
                "bouillon",
                25,
                "    Dispensing cup \n    Dispensing bouillonPowder \n    Dispensing water"
            )
        ]

    def select(self, choiceIndex):
        chosenProduct = self.products[choiceIndex]
        chosenProductCost = chosenProduct.getPrice()
        if self.cashBox.haveYou(chosenProductCost):
            self.cashBox.deductFromCredit(chosenProductCost)
            chosenProduct.make()
            if self.cashBox.credit > 0:
                self.cashBox.returnCoins(self.cashBox.credit)
        else:
            print("Sorry. Not enough money deposited.")


class Product:
    def __init__(self, name, price, recipe):
        self.name = name
        self.price = price
        self.recipe = recipe

    def getPrice(self):
        return self.price

    def make(self):
        print(f"Making {self.name}:")
        print(self.recipe)


def main():
    cm = CoffeeMachine()
    while cm.oneAction():
        pass
    total = cm.totalCash()
    print(f"Total cash: ${(total / 100):.2f}")

if __name__ == "__main__":
    main()