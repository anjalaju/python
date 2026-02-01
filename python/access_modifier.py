class Demo:
    _name="Anjal"
    def hi(self):
        self.__hello()
        print("Welcome to my class")
    def _welcome(self):
        print("Welcome to my class")
    def __hello(self):
        print("hello world")
x=Demo()
print(x._name)
x.hi()
x._welcome()



