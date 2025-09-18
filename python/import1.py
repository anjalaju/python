class student1:
    def __init__(self):
        self.name=input("Enter a name :")
        self.english=int(input("Enter a mark of english :"))
        self.maths=int(input("Enter a mark of maths :"))
        self.computer=int(input("Enter a mark of computer :"))
        self.physics=int(input("Enter a mark of physics :"))
        self.malayalam=int(input("Enter a mark of malayalam :"))
    def sum(self):
        total=self.english + self.computer +self.malayalam + self.maths + self.physics
        print("Total mark :",total)
    def average(self):
        avgg= self.english + self.computer +self.malayalam + self.maths + self.physics
        avgg= avgg/5
        return avgg
    def display(self):
        print("Student name is :",self.name)
        print("Mark of english is :",self.english)
        print("Mark of maths is :",self.maths)
        print("Mark of malayalam is :",self.malayalam)
        print("Mark of physics is :",self.physics)
        print("Mark of computer is :",self.computer)
        print("*"*70)
