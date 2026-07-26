from bank_account import BankAccount


class User:

    def __init__(self, name, email=""):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}", end=", ")
        self.account.display_account_info()
        return self



user1 = User("Bara")
user1.make_deposit(100).make_deposit(200).make_withdrawal(50).display_user_balance()