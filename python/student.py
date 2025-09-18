class student:
    def __init__(self):
        self.name=input("Enter the name: ")
        self.english=int(input("Enter the mark of english: "))
        self.maths=int(input("Enter the mark of maths: "))
        self.computer=int(input("Enter the mark of computer: "))
        self.physics=int(input("Enter the mark of physics: "))
        self.malayalam=int(input("Enter the mark of malayalam: "))

    def sum(self):
        total=self.english + self.computer +self.malayalam + self.maths + self.physics
        print("The Total mark is:",total)

    def average(self):
        avg=self.english + self.computer +self.malayalam + self.maths + self.physics
        avg=avg/5
        print("The average of the mark is:",avg)
        return avg
    def display(self):
        # print("The name is:",self.name,self.english,self.computer,self.malayalam,self.maths,self.physics)
        print("The student name is :",self.name)
        print("English mark:",self.english)
        print("Computer mark:",self.computer)
        print("Malayalam mark:",self.malayalam)
        print("Maths mark:",self.maths)
        print("Pysics mark:",self.physics)

class child(student):
    def grade(self):
        avg=self.average()
        if avg>90:
          print("The grade is A+")
        elif avg>80:
            print("The grade is A")
        elif avg>70:
            print("The grade is B+")
        elif avg>60:
            print("The grade is B")
        elif avg>50:
            print("The grade is C+")
        elif avg>40:
            print("The grade is C")
        elif avg>30:
            print("The grade is D+")
x=child()
x.sum()
x.grade()
x.average()
x.display()