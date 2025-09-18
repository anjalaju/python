def hello():
    print("Hello everyone")
def hi():
    print("hi everyone")
def surpise():
    print("hi surprise everyone")
list1 = [21, 23, 45, 65, 67, 97, 54]
def add():
    summ = 0
    for i in list1:
        print(i)
        summ = summ + i
    return summ
add_sum = add()
print("The sum is:", add_sum)