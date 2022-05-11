test = print("Hello")

if(None == test):
    print("Yes",'\nHello',end='') #Stops autonewline
    print("\nChris", "Mei", "Carl",sep=':') #Adds seperators

def spam():
    global eggs #Uses global variable
    eggs = "Spam local"

spam()
print(eggs)
