def spam():
    global eggs
    eggs = "I am a global"

def bacon():
    eggs = "I am a local variable"

def ham():
    print(eggs) #I will be a global variable

eggs = 42
spam() 
print(eggs)