name =''
while name != 'your name':
    print("Please input your name")
    name = input()

print ("Thank you!")

while True:
    print("Please enter your age")
    name = input()
    if name == "your age":
     break

print("Thank you")


while True:
    print("What's your name?")
    name = input()

    if name != "Chris":
     continue #returns to the beginning of fthe loop
 
    print("Hello "+ name +", What's your password?")
    password = input()
    
    if password == "password":
     break

print("Welcome!")
