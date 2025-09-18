# class bank_account:
#     __bank_balance=25000

#     def __init__(self):
#         self.bank_balance=25000
#         print("welcome")

#     def acc_no(self):
#         print("account number is AC-12345678910")

#     def acc_holder(self):
#         print("Anjal")
# class withdrawl(bank_account):

#     def withdraw(self,amount):
#         if(amount<=self.bank_balance):
#             self.bank_balance=self.bank_balance-amount
#             print("withdrawl successful.....!Remaining balance is ",self.bank_balance)
#         else:
#             print("insufficient balance")

# class deposit(withdrawl):
#     def depo(self,amount):
#         self.bank_balance=self.bank_balance+amount
#         print("Deposit successful.....!current balance is ",self.bank_balance)

# x=deposit()
# x.depo(3000)




class Bankaccount:
    def __init__(self, account_number, balance, name):
        self._account_number=account_number
        self.__balance=balance
        self.name=name

    def deposit(self, amount):
        self.__balance+=amount
        print("deposited", amount, "newbalance:", self.__balance)

    def withdraw(self, amount):
        if amount>self.__balance:
            print("not enough money")
        else:
            self.__balance-=amount
            print("withdraw", amount, "new balance:", self.__balance)

    def show_details(self):
        print("account holder name:", self.name)
        print("account number:", self._account_number)

acc=Bankaccount(123456789, 1000, "Anjal")
acc.deposit(200)
acc.withdraw(200)