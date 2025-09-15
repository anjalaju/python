list1=[55,97,64,98,43,62,82]
def average():
    add=0
    for i in list1:
        print(i)
        add=add+i
    return add//len(list1)
avgg=average()
print("The average is:",avgg)