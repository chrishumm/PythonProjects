GreetingMessage= ["Hello\nWhat is your name?", "It is nice to meet you, ", "","What is your age?"]

def greet():
 counter= 0;
 while counter < 4:
  if counter < 1:
   print(GreetingMessage[counter])
  elif counter == 1:
   GreetingMessage[counter+1] = input()
   print(GreetingMessage[counter] + GreetingMessage[counter+1])
   counter+=1
  elif counter < 3:
   print(GreetingMessage[counter]) 
  counter+=1

def askAge():
 print(GreetingMessage[3])
 myAge = input()
 print('You will be ' + str(int(myAge)+ 1) + ' in a year.')
 
def calcNameLength():
 myName = GreetingMessage[2]
 print('The length of your name is: ')
 print(len(myName))

 
 
greet()
calcNameLength()
askAge()


