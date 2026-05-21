from abc import ABC, abstractmethod

class BankAccount(ABC):
    def __init__(self, account_number, owner, initial_balance=0):
        self.account_number = account_number
        self.owner = owner
        self.__balance = initial_balance #private attribute

    def getBalance(self):
        return self.__balance
    def _update_balance(self, amount):
        self.__balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass

    def deposit(self, amount):
        if amount > 0:
            self._update_balance(amount)
            print(f"{self.owner} deposited {amount}. New Balance: {self.getBalance()}")
        else:
            print("Invalid amount")

class CheckingAccount(BankAccount):
    def __init__(self, account_number, owner, initial_balance=0, overdraft_limit=100):
        super().__init__(account_number, owner, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.getBalance() + self.overdraft_limit:
            self._update_balance(-amount)
            print(f"{self.owner} withdrew {amount} from Checking. New Balance: {self.getBalance()}")
        else:
            print("Insufficient Balance")

class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if amount <= self.getBalance():
            self._update_balance(-amount)
            print(f"{self.owner} withdrew {amount} from Savings. New Balance: {self.getBalance()}")
        else:
            print("Insufficient Balance")


if __name__ == "__main__":
    savings = SavingsAccount("S001", "Penguin", 100)
    savings.deposit(100)
    print(savings.getBalance())
    savings.withdraw(150)
    print(savings.getBalance())