class PrivateExample:
    def __init__(self):
        self.__myHiddenVal = 1
        self.myPublicVal = 2



p = PrivateExample()
p.myPublicVal
# p.__myHiddenVal #will throw AttributeError
p._PrivateExample__myHiddenVal