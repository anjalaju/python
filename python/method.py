num1=input("Enter the first no : ")
num2=input("Enter the second no : ")
method=input("Enter the method(+,-,/,*) :")
x=int(num1)
y=int(num2)
print("-"*50)
if method== "+" :
    print("The result is :"+ str(x+y))
elif method== "-" :
    print("The result is :"+ str(x-y))
elif method== "*" :
    print("The result is :"+ str(x*y))
elif method== "/" :
    print("The result is :"+ str(x/y))
print("-"*50)