class BankAccount:
    accounts = []

    def __init__(self, balance, int_rate, account_type):
        self.int_rate = int_rate
        self.balance = balance
        self.account_type = account_type
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
        print(f"Account: {self.account_type}")
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

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {}

    def open_new_account(self, initial_amount, interest, account_type):
        self.account[account_type] = BankAccount(initial_amount, interest, account_type)
        print(f"Your new account {account_type} has been created.")
        print(f"Your starting balance is ${initial_amount}")
        return self

    def make_deposit(self, amount):
        self.account.balance += amount
        print(f"Deposit: ${amount} New Balance: ${self.account.balance}")
        return self

    def make_withdrawl(self, amount):
        if ((self.account.balance - amount) < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.account.balance -= (amount + 5)
            print(f"Withdrawl ${amount} New balance with fee: ${self.account.balance}")
            # return self
        else:
            self.account.balance -= amount
            print(f"Withdrawl: ${amount} New Balance: ${self.account.balance}")
        return self

    def display_user_balance(self, account_type):
        print(f"{self.name}, your current balance is: ${self.account.balance}")
        return self

    def transfer(self, account_type , amount, other):
        self.account[account_type].balance -= amount
        other.balance += amount

# user1 = BankAccount(.05,500)
# user2 = BankAccount(.03,1000)

Chris = User("Chris", "chris@aol.com")
# Chris.account = BankAccount(.05,1000,"savings")
# Chris.display_user_balance()

Chris.open_new_account(200, .01, "checking")
Chris.open_new_account(1000, .01, "savings")
# print(Chris.account)
Chris.transfer("checking", 100, Chris.account["savings"])
print(Chris.account["checking"].balance, Chris.account["savings"].balance)
# Chris.make_withdrawl(200)

# Renee = User("Renee", "renee@aol.com")
# Renee.account = BankAccount(.02,2000)

# Chris.transfer(100)
# Renee.display_user_balance()


# user1.deposit(100).deposit(500).deposit(1000).withdraw(1500).yield_interest().display_account_info
# user2.deposit(200).deposit(400).withdraw(50).withdraw(300).withdraw(500).withdraw(1000).yield_interest().display_account_info()

# BankAccount.all_account_info()