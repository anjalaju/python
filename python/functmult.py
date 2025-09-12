def table(x,y):
    if y==0:
        return
    table(x,y-1)
    print(y,"*",x,"=",x*y)
max=10
table(2,max)