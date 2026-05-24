
# for public attribute self.name
#  for protected attribute self._name
# for private attribute self.__name

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance= balance

    def get_balance(self):
        return self.__balance
    

a1 = Bank('rajiv',2000)
print(a1.name, a1.get_balance())