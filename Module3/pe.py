"""
File: taxformwithgui.py
Project 8.1
A GUI-based tax calculator.

Computes and prints the total tax, given the income and
number of dependents (inputs), and a standard deduction of
$10,000, an exemption amount of $3,000, and a flat tax rate
of 20%.
"""

from breezypythongui import EasyFrame

class TaxCalculator(EasyFrame):
    """Application window for the tax calculator."""

    def __init__(self):
        """Sets up the window and the widgets."""
        EasyFrame.__init__(self, title = "Tax Calculator")
        self.standardDeduction = 10000
        self.exemptionPerDependent = 3000
        self.taxRate = .2
        self.taxToDisplay = 0.0

        # Label and field for the income
        self.incomeField = self.addLabel(text = "Gross income", row=0, column=0)
        self.incomeField = self.addFloatField(value = "0.0", row=0, column =1)

        # Label and field for the number of dependents
        self.depFieldLabel = self.addLabel(text="Dependents", row=1, column=0)
        self.depField = self.addIntegerField(value = "0.0", row = 1, column = 1)

        # The command button
        self.actionButton = self.addButton(text="Compute", command = self.computeTax, row=3, column=2)

        # Label and field for the tax
        self.taxFieldLabel = self.addLabel(text="Total tax", row=4, column=0)
        self.taxField = self.addFloatField(value=self.taxToDisplay, row=4, column=2)

    # The event handler method for the button
    # Computes and prints the total tax, given the income and
# number of dependents (inputs), and a standard deduction of
# $10,000, an exemption amount of $3,000, and a flat tax rate
# of 20%.
    def computeTax(self):
        """Obtains the data from the input field and uses
        them to compute the tax, which is sent to the
        output field."""
        income = self.incomeField.getNumber()
        dependents = self.depField.getNumber()
        dependentExemption = dependents * self.exemptionPerDependent
        tax = (income - self.standardDeduction - dependentExemption) * self.taxRate
        self.taxToDisplay = tax
        self.taxField.setNumber(tax)
        return netTax


def main():
    TaxCalculator().mainloop()

if __name__ == "__main__":
    main()

