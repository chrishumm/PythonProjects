import random
import pyinputplus as pyin

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ["]","[","#","$","*","@"]
numbers = ['0','1','2','3','4','5','6','7','8','9']
print("Welcome to the PyPasswordGenerator!")

password_length = pyin.inputInt("How long do you want your password to be?")
number_of_letters = pyin.inputInt("How many letters do you want in your password?", lessThan=password_length)
number_of_symbols = pyin.inputInt("How many symbols do you want in your password?", lessThan=(password_length+1) - number_of_letters, greaterThan=-1)
number_of_numbers = pyin.inputInt("How many numbers do you want in your password?",greaterThan=-1, lessThan=password_length+1 - number_of_letters - number_of_symbols)

new_password = ""
for i in range(1,number_of_letters):
    new_password+= random.choice(letters)
for i in range(1,number_of_numbers):
    new_password += random.choice(numbers)
for i in range(1,number_of_symbols):
    new_password += random.choice(symbols)

    
random_order = random.sample(new_password,len(new_password))
new_password = ""
for i, value in enumerate(random_order):
    new_password += value   

print(new_password)

def foo(a, b=4, c=6):
    print(a, b, c)
 
foo(20, c=12)
55


