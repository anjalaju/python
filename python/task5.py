text=input("Enter a string : ")
reverse=""
for i in range(len(text) -1, -1, -1 ):
    reverse += text[i]
print("Reverse:",reverse)