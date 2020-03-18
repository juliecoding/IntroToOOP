class Bank():
    def __init__(self):
        self.accounts = []

    def __str__(self):
        result = ""
        for account in self.accounts:
            result += str(account)
            result += '\n'
        return result

    def add(self, account):
        self.accounts.append(account)
        # return self.accounts[-1]

    def get(self, name, pin):
        for account in self.accounts:
            if account.getName() == name and account.getPin() == pin:
                return account
        # return self.accounts

    def remove(self, name, pin):
        for account in self.accounts:
            if account.getName() == name and account.getPin() == pin:
                self.accounts.remove(account)
        return self.accounts
        # return self.accounts

    def computeInterest(self):
        totalInterest = 0.0
        for account in self.accounts:
            totalInterest += account.computeInterest()
        return totalInterest


class SavingsAccount():
    #STATIC VARIABLES
    RATE = 0.02
    MIN_BALANCE = 25

    def __init__(self, name, pin, balance = 0.0):
        self.name = name
        self.pin = pin
        self.balance = balance

    def __str__(self):
        result = 'Name: ' + self.name + '\n'
        result += 'PIN: ' + str(self.pin) + '\n'
        result += 'Balance: ' + str(self.balance)
        return result

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            return "Amount must be >= 0"
        if amount - self.balance < 0:
            return "Invalid, withdraw more than " + str(self.balance)
        else:
            self.balance -= amount
            return str(self.balance)

    def getBalance(self):
        return self.balance

    def getName(self):
        return self.name

    def getPin(self):
        return self.pin

    def computeInterest(self):
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)

    def computeInterest(self):
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest


    @staticmethod #function decorator
    def getRate(): #NOTE: no `self`!
        return SavingsAccount.RATE



bank = Bank()

savings1 = SavingsAccount("Julie", "1", 10000.00)
savings2 = SavingsAccount("Alan", "2", 5000.00)

""" FOR A GOOD TIME, UNCOMMENT: """
# savings2.RATE = 4 #This is really bad. Look what happens:
# print(savings1.getRate()) #0.02
# print(savings2.getRate()) #0.02
# print(savings2.RATE)      #4
# SavingsAccount.RATE = 8
# print(SavingsAccount.RATE) #8
# print(savings2.getRate())  #8
# print(savings2.RATE)  #4

# print(SavingsAccount.getRate()) #THIS IS VALID
#print(SavingsAccount.withdraw(30)) #Doesn't work because withdraw is not a static method

bank.add(savings1)
bank.add(SavingsAccount("Jacob", "2", 650))
bank.add(SavingsAccount("Scott", "3", 9489392))

print("BEFORE INTEREST", bank)
totalInterestForBankThisQuarter = bank.computeInterest()
print(totalInterestForBankThisQuarter)
print("AFTER INTEREST", bank)