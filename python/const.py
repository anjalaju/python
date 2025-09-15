class operations:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def sum(self):
        print(f"sum of two number is:{self.num1+self.num2}")
    def sub(self):
        print(f"sub of two number is:{self.num1-self.num2}")
    def mul(self,num3):
        print(f"mul of two number is:{self.num1*self.num2*num3}")
        print("*"*70)
cal=operations(5,5)
cal.sum()
cal.mul(5)