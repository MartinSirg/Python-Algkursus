"""Simple bank."""


class Account:
    """Represent a bank account."""

    def __init__(self, name, balance):
        """
        Class constructor. Each account has owner's name and starting balance.

        :param name: account owner name. String.
        :param balance: starting balance of account. Integer.
        """
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """
        Withdraw money from account.

        :param amount: amount to withdraw from account, has to be positive
        and the balance can't go below 0.
        """
        if amount > self.balance:
            self.balance = 0
        elif amount < 0:
            self.balance = self.balance
        else:
            self.balance -= amount

    def deposit(self, amount):
        """
        Deposit money to account.

        :param amount: amount to deposit to account, has to be positive
        """
        if amount < 0:
            self.balance = self.balance
        else:
            self.balance += amount

    def get_balance(self):
        """
        Get account balance.

        :return: balance in double form
        """
        return self.balance

    def get_name(self):
        """
        Get account owner name.

        :return: owner name in string form
        """
        return self.name


# Creating the Account class instance and giving it name, starting balance
paul_account = Account("Paul", 100.00)
jakob_account = Account("Jakob", 500.00)

print("Initial balance")
print(paul_account.get_balance())  # 100.0
print(jakob_account.get_balance())  # 500.0

assert paul_account.get_balance() == 100
assert jakob_account.get_balance() == 500

jakob_account.withdraw(250.00)
assert jakob_account.get_balance() == 250
print("Jakob's balance is now ", jakob_account.get_balance())  # Jakob's balance is now  250.0
paul_account.deposit(250.00)
assert paul_account.get_balance() == 350
print("Paul's balance is now", paul_account.get_balance())  # Paul's balance is now 350.0

print("Final state")
print(paul_account.get_balance())  # 350.0
print(jakob_account.get_balance())  # 250.0"""
