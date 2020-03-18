class ResponseDialog(EasyDialog):
    def __init__(self, parent, title):
        EasyDialog.__init__(self, parent, title)

    def body(self, parent):
        self.addLabel(parent, text = "First:", row = 0, column = 0)
