# from operator import itemgetter

# params = {'a': 1, 'b': 2}

# a, b = itemgetter('a', 'b')(params)
from breezypythongui import EasyFrame
import math

class NumberFieldDemo(EasyFrame):
    def __init__(self):
        #What am I passing to/as self??
        EasyFrame.__init__(self)
        self.addLabel("An integer", row = 0, column = 0)
        self.inputField = self.addIntegerField(0, 0, 1, width = 10)
        sqrtLabel = self.addLabel("Square root", 1, 0)
        self.outputField = self.addFloatField(value = 0.0, row = 1, column = 1, width = 8, precision = 2, state = "readonly")
        self.addButton(text="Compute", row = 2, column = 0, columnspan = 2, command = self.computeSqrt)


    def computeSqrt(self):
        number = self.inputField.getNumber()
        result = math.sqrt(number)
        self.outputField.setNumber(result)

def main():
    NumberFieldDemo().mainloop()




if __name__ == "__main__":
    main()