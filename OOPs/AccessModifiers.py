class Account:
    __amount=0
     def deposit(self, add):
        self.__amount +=add

    def debit(self,sub):
        self.__amount -=sub

    def printAmount(self):
        print(self.__amount)

class User(Account):
    def calculateTax(self):
            tax = self._amount*1.2
            print(tax)
u1 = User()
h1 = deposit(100)
b1.printAmount()
b1.debit(50)
