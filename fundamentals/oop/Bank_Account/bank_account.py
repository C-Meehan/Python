class BankAccount:
    accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit: ${amount} New Balance: ${self.balance}")
        return self

    def withdraw(self, amount):
        if ((self.balance - amount) < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= (amount + 5)
            print(f"Withdrawl ${amount} New balance with fee: ${self.balance}")
            return self
        else:
            self.balance -= amount
            print(f"Withdrawl: ${amount} New Balance: ${self.balance}")
            return self

    def display_account_info(self):
        print(f"Current Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance += (self.balance * self.int_rate)
            print(f"Current balance with yielded interest: ${self.balance}")
        return self

    @classmethod
    def all_account_info(cls):
        for account in cls.accounts:
            account.display_account_info()

user1 = BankAccount(.05,500)
user2 = BankAccount(.03,1000)

user1.deposit(100).deposit(500).deposit(1000).withdraw(1500).yield_interest().display_account_info
user2.deposit(200).deposit(400).withdraw(50).withdraw(300).withdraw(500).withdraw(1000).yield_interest().display_account_info()

BankAccount.all_account_info()

# user1.withdraw()
# user1.display_account_info()
# user1.yield_interest()