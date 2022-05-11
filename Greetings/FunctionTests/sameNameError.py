def spam():
    print(eggs) #Local variable doesn't exist in scope 
    eggs = 'spam local'

eggs = 'global'
spam()