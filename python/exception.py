try:
    x=int(input("Enter a number"))
    y=int(input("Enter a number"))
    print("sum of numberis:",x/y)
except ZeroDivisionError:
    print("cant divide by zero")
except Exception as e:
    print("you got an error",e)
finally:
    print("called")