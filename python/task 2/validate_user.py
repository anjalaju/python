

firstnum=input("Enter the first num:\n")
lastnum=input("Enter the second num:\n")
print("*"*100)
if firstnum.isalpha() or lastnum.isalpha():
    print("Please enter a valid integer")
    print("*"*100)
else:
    firstnum=int(firstnum)
    lastnum=int(lastnum)
    print("The result is: " + str(firstnum + lastnum))
    print("*"*100)

    

    # num1=input("Enter the first no : ")
# num2=input("Enter the second no : ")
# x=int(num1)
# y=int(num2)
# result=x+y
# print("-"*50)
# print("The result is :"+ str(result)) 
# print("-"*50)
