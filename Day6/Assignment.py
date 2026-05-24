class Bank:
    def __init__(self, acc_num, owner, balance):
        self.acc_num = acc_num
        self.owner = owner
        self.balance = balance
    @staticmethod
    def withdraw(balance):
        n = int(input("enter the amount u want to withdraw"))
        balance= balance-n