GreetingMessage= ["Hello\nWhat is your name?", "It is nice to meet you, ", "","What is your age?"]
name = 2

def greet():
 counter = 0
 while counter < 4:
  if counter < 1:
   print(GreetingMessage[counter])
  elif counter == 1:
   GreetingMessage[name] = input()
   print(GreetingMessage[1] + GreetingMessage[name])
  elif counter < 3:
   print(GreetingMessage[counter]) 
   
  counter+=1

def askAge():
 print(GreetingMessage[3])
 myAge = input()
 print('You will be ' + str(int(myAge)+1) + ' in a year.')
 
def calcNameLength():
 print('The length of your name is: '+ str(len(GreetingMessage[name])))

 
greet()
calcNameLength()
askAge()
exit()


