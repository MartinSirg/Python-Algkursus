"""Bank account."""


class BankAccount:
    """Represent a bank account."""

    def __init__(self, name: str, balance: float):
        """Define name and balance within BankAccount."""
        if balance < 0:
            balance = 0
        self.balance = balance
        self.name = name

    def withdraw(self, amount: float):
        """
        Withdraw money from bank account.

        If account has less balance than the specified amount, return False
        If specified amount is less than 0 return False
        Otherwise change the balance and return True
        :param amount: amount to be deducted from balance
        """
        if self.balance < amount:
            return False
        elif amount < 0:
            return False
        else:
            self.balance -= amount
            return True

    def deposit(self, amount: float):
        """Add amount to balance, unless amount is negative."""
        if amount < 0:
            self.balance = self.balance
        else:
            self.balance += amount

    def get_balance(self):
        """Return balance."""
        return self.balance

    def get_name(self):
        """Return bank account owner's name."""
        return self.name

    def transfer(self, target, amount, fee=0.01):
        """
        Transfer money to another BankAccount object.

        If amount and fee sum is less than bank account balance, dont transfer and return False
        If name of both accounts is the same, then the fee is half
        If transfer target is the same account, fee is 0
        :param target: target BankAccount object
        :param amount:  amount to be transferred
        :param fee: fee that will be deducted from transferrers account
        :return: True if transfer is successful
        """
        try:
            target_name = target.get_name()
        except AttributeError:
            return False
        if self.get_name() == target_name:
            fee = fee / 2
        if target == self:
            fee = 0
        if amount + (amount * fee) < self.get_balance():
            self.withdraw(amount + (amount * fee))
            target.deposit(amount)
            return True
        else:
            return False
