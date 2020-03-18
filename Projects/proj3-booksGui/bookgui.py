from breezypythongui import EasyFrame
from breezypythongui import EasyDialog
import bookrecs


class BookDialog(EasyDialog):
    def __init__(self, parent, title):
        EasyDialog.__init__(self, parent, title)

    def body(self, parent):
        self.labelReader = self.addLabel(text = "Reader", master = parent, row = 0, column = 0)
        self.inputReader = self.addTextField(master = parent, row = 0, column = 1, text="")
        self.labelFriends = self.addLabel(text = "# of friends", master = parent, row = 1, column = 0)
        self.inputFriends = self.addIntegerField(master = parent, row = 1, column = 1, value=2)

    def validate(self):
        try:
            reader = self.inputReader.getText()
            num = self.inputFriends.getNumber()
        except:
            self.messageBox(title = "Error", message = "Reader must exist. Friends must be greater than zero.")
            return False
        if reader not in bookrecs.ratings:
            self.messageBox(title = "Error", message = "No such reader")
            return False
        elif num <= 0:
            self.messageBox(title = "Error", message = "Friends must be greater than 0")
            return False
        return True

    def apply(self):
        self.setModified()

class BookGui(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)

        self.setBackground('powder blue')
        btnFriends = self.addButton(text = "Friends", command = self.openFriendsDialog, row = 0, column = 0)
        btnRecommend = self.addButton(text = "Recommend", row = 0, column = 1, command = self.openRecommendationsDialog)
        btnReport = self.addButton(text = "Report", row = 0, column = 2, command = self.displayReport)

    def openFriendsDialog(self):
        dialogBox = BookDialog(self, "Friends")
        if dialogBox.modified():
            person = dialogBox.inputReader.getText()
            nFriends = dialogBox.inputFriends.getNumber()
            friends = '\n'.join(bookrecs.friends(person, nFriends))
            self.messageBox(title = f"Friends of {person}", message = friends, width = 100, height = 20)

    def openRecommendationsDialog(self):
        dialogBox = BookDialog(self, "Recommendations")
        if dialogBox.modified():
            person = dialogBox.inputReader.getText()
            nFriends = dialogBox.inputFriends.getNumber()
            recString = ''
            recs = bookrecs.recommend(person, nFriends)
            for rec in recs:
                recString += rec[0] + ', ' + rec[1] + '\n'
            self.messageBox(title = f"Recommendations for {person}", message = recString, width = 100, height = 20)

    def displayReport(self):
        report = bookrecs.report()
        self.messageBox(title = "Report", message=report, width = 100, height = 50)


def main():
    BookGui().mainloop()

if __name__ == "__main__":
    main()