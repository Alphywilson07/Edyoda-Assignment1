class Account:
    def __init__(self, title, balance=0):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
        
acc = Account("Ashish", 5000)
print(acc.title)  # Output: Ashish
print(acc.balance)  # Output: 5000

savings_acc = SavingsAccount("Ashish", 5000, 5)
print(savings_acc.title)  # Output: Ashish
print(savings_acc.balance)  # Output: 5000
print(savings_acc.interestRate)  # Output: 5
