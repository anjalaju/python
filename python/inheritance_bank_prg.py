class bank_account:
    __bank_balance=25000

    def __init__(self):
        self.bank_balance=25000
        print("welcome")

    def acc_no(self):
        print("account number is AC-12345678910")

    def acc_holder(self):
        print("Anjal")
class withdrawl(bank_account):

    def withdraw(self,amount):
        if(amount<=self.bank_balance):
            self.bank_balance=self.bank_balance-amount
            print("withdrawl successful.....!Remaining balance is ",self.bank_balance)
        else:
            print("insufficient balance")

class deposit(withdrawl):
    def depo(self,amount):
        self.bank_balance=self.bank_balance+amount
        print("Deposit successful.....!current balance is ",self.bank_balance)

x=deposit()
x.depo(3000)