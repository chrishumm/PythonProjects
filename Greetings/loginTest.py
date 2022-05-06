print('Please enter your username')
name = input()
print('Please enter your password')
password= input()

def welcomeMessage(result):
 if(result == False):   
  print('Access Denied')
 else:
  print('Access Granted')

if (name == 'Chris') and (password == 'test'):
 print('Hello, '+ name)
 welcomeMessage(True)
elif(name != 'Chris'):
 print('Wrong username.')
 welcomeMessage(False)
else:
 print('Wrong password')
 welcomeMessage(False)


 #Python if statements use colons at the end of if/elif/else
 
