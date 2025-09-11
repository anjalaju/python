num=987
rev=0
while num > 0:
   n=num%10
   num=num//10   
   rev=rev*10+n
print(rev)