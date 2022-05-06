print("What's your name?")
name = input()
print("How old are you?")
ageCheck = False

#Santiy checks with isnumeric()
#Simple while loop
while(ageCheck == False):
 age = input()
 if(age.isnumeric() == True):
  ageCheck = True
  age = int(age)
 else:
  print("Please enter a numeric value")

if name == 'Chris' and age == 29:
    print('Hi, ' + name)
elif age < 12:
    print('You are too young to be ' +name+'.')
elif age > 2000:
    print(name+' is not an immortal vampire.')
elif age > 100:
    print(name+"isn't my grandfather!")
