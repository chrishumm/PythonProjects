import random

#All messages contained in this tuple
eightBall_messages = ('It is certain',
'It is decidely so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again'
'My reply is no'
'Outlook not so good'
'Very doubtful')

while True:
        
    print("Write your question and ask the magic eightball or (q)uit")

    input_response = input()
    if(input_response == "q" or input_response == "Q"):
        break
    print(random.choice(eightBall_messages))