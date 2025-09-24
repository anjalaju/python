from os import *
print(getcwd())
print(listdir())
makedirs("scope/scope/scopeindia")
removedirs("scope/scope/scopeindia")
rename("file_re.py","file_file.py")
print(path.exists("student.py"))


from csv import *
with open("akhil.txt","r+") as file:
    reader=reader(file)
    for i in reader:
        print(i)

from csv import *
with open("akhil.txt","w+") as file:
    x=["id","Name","age","country"]
    writer=DictWriter(file,fieldnames=x)
    writer.writeheader()
    writer.writerow({"id":101,"Name":"Akash","age":21,"country":"india"})
    writer.writerow({"id":102,"Name":"Anil","age":24,"country":"india"})
    writer.writerow({"id":103,"Name":"Akhil","age":26,"country":"india"}) 

from datetime import *
print("current date and time is :",datetime.now())
print("or like this :",datetime.now().strftime("%y"))
print("day number of a year is:",datetime.now().strftime("%j"))
print("time and date is :",datetime.now().strftime("%x-%X"))
print("month name in short version :",datetime.now().strftime("%b"))
print("in microsecond :",datetime.now().strftime("%f"))
print("like this :",datetime.now().strftime("%y-%m-%d-%H-%M"))


from tkinter import *
main=Tk()
main.title("My webpage")
main.geometry("800x600")
main.mainloop()