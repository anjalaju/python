try:
    x=int(input("Enter a number"))
    y=int(input("Enter a number"))
    print("sum of number is:",x/y)
except ZeroDivisionError:
    print("cant divide by zero")
except Exception as e:
    print("you got an error",e)
finally:
    print("called")