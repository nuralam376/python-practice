class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance
    

account1 = BankAccount("Abc", 1_00_000)

account1.set_balance(2_00_000)
print(account1.name, account1.get_balance())
print(account1._BankAccount__balance)
