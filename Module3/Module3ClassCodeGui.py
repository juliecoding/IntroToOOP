from breezypythongui import EasyFrame

class Module3GuiCode(EasyFrame):
    def __init__(self):
        #could also be
        # super().__init__()
        EasyFrame.__init__(self,
                            title="Module 3 Class Code",
                            width=500,
                            height=300,
                            background='green')
        self.colorCounter = 0
        self.addLabel(text = "(0, 0)", row = 0, column = 0, sticky="NSEW", background="black") #Centers the label. North, South, East West
        # self.addLabel(text = "(1, 0)", row = 1, column = 0)
        # self.addLabel(text = "(0, 1)", row = 0, column = 1)
        # self.addLabel(text = "(1, 1)", row = 1, column = 1)
        self.btnChangeColor = self.addButton(text = "Click me", row = 0, column = 1, columnspan = 2, command = self.changeColor)
        self.txtBackgroundColor = self.addTextField(text = "green", row = 1, column = 1, columnspan = 2)
        self.lblLC = self.addLabel(text="Label color", row = 2, column = 0, background = "pink")
        self.txtLabelColor = self.addTextField(text = 'green', row = 2, column = 1, columnspan = 2)

    def changeColor(self):
        """if self.colorCounter == 0:
            self.setBackground('green')
            self.addLabel(text="Purple label", row = 0, column = 0, sticky = "NSEW", background = "purple")
            self.colorCounter += 1
        elif self.colorCounter == 1:
            self.setBackground('yellow')
            self.addLabel(text="Orange label", row = 0, column = 0, sticky = "NSEW", background="orange")
            self.colorCounter += 1
        else:
            self.setBackground('blue')
            self.addLabel(text = 'Green Label', row = 0, column = 0, sticky = "NSEW", background = "green")
            self.colorCounter = 0"""
        newBackgroundColor = self.txtBackgroundColor.getText()
        newLabelColor = self.txtLabelColor.getText()

        self.setBackground(newBackgroundColor)
        self["lblOne"]["text"] = newLabelColor.capitalize() + " Label"
        self.lblOne.background = newLabelColor
        self.lblLC = newLabelColor


def main():
    Module3GuiCode().mainloop()

if __name__ == "__main__":
    main()