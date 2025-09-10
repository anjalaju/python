age=int(input("Enter the age : "))
print("-"*50)
if age >=1 and age <=12 :
    print("You are in child")
    print("-"*50)
elif age >=13 and age <=19 :
    print("You are in teenage")
    print("-"*50)
elif age >=20 and age <=40 :
    print("You are in adult")
    print("-"*50)
elif age >=40 and age <=60 :
    print("You are in elder")
    print("-"*50)
else :
    print("You are in senior")
    print("-"*50)