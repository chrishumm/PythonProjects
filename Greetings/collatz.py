
def integer_input():
    print("Please enter a number")
    try:
        user_number = int(input())
        return user_number
    except ValueError:
       print("Please enter a valid integer")
       return None

def collatz(number):
    if(number % 2 == 0):
        print(number // 2)
        return number // 2
    elif(number % 2 == 1):
        print(3*number+1)
        return(3*number+1)
    else:
        print("Error")
while True:
    user_number = integer_input()
    if(user_number != None):
        break

while user_number != 1:
    user_number = collatz(user_number)
