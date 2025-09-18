     
from import1 import *
class child(student1):
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