
def parent(name):       
    cash = 10
    def play():
        nonlocal cash
        cash = cash - 1
        print("balance cash:", name, ":", cash)
    return play  
boy = parent("Anjal")
girl = parent("Alana")
boy()
girl()
boy() 
boy()
