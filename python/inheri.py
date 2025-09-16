# class demo:
#     def hello(self):
#         print("hello world")
#     def hi(self):
#         print("hiiiii")
# x=demo()
# x.hello()
# x.hi()

# class demo:
#     def hello(self):
#         print("hello world")
#     def hi(self):
#         print("hiii")
# class child(demo):
#     def house(self):
#         print("This is the house")
# class child2(child):
#     def home(self):
#         print("This is the home")

# x=child2()
# x.hello()
# x.house()
# x.home()


# class demo:
#     name="anjal"
#     def hello(self):
#         print("hello world")
#     def hi(self):
#         print("hiii")
# class child(demo):
#     def house(self):
#         print("This is the house")
# class child2(child):
#     def home(self):
#         print("This is the home")

# x=child2()
# x.hello()
# x.house()
# x.home()
# print(x.name)



class main:
    def menu(self):
        print("This is the main ")
class demo:
    name="anjal"
    def hello(self):
        print("hello world")
    def hi(self):
        print("hiii")
class child(demo):
    def house(self):
        print("This is the house")
class child2(child,main):
    def home(self):
        print("This is the home")

x=child2()
x.hello()
x.house()
x.home()
print(x.name)
x.menu()