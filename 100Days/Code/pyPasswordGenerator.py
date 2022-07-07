from cmath import e
import random
import re
from unicodedata import numeric
import pyinputplus as pyin

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ["]","[","#","$","*","@"]
print("Welcome to the PyPasswordGenerator!")

while True:
    password_length = pyin.inputInt("How long do you want your password to be?")
    number_of_letters = pyin.inputInt("How many letters do you want in your password?", lessThan=password_length)
    number_of_symbols = pyin.inputInt("How many symbols do you want in your password?", lessThan=(password_length+1) - number_of_letters, greaterThan=-1)
    number_of_numbers = pyin.inputInt("How many numbers do you want in your password?",greaterThan=-1)

    if(number_of_letters+number_of_symbols+number_of_numbers > password_length):
        print(f"Please make sure they add up to {password_length}")
    if(number_of_letters+number_of_symbols+number_of_numbers < password_length):
        print(f"Please make sure they add up to {password_length}")

    else:
        break

passwordString = ""
chosenNumber = 0
chosenSymbol = 0
chosenLetter = 0

for i in range(password_length):
    possible_choices = ['Symbol', 'Letter', "Number"]
    while True:
     choice = random.choice(possible_choices)
     if(choice == 'Symbol' and chosenSymbol < number_of_symbols):
        passwordString+=random.choice(symbols)
        chosenSymbol+=1
        break
     elif choice == 'Symbol' and chosenSymbol == number_of_symbols:
        possible_choices.remove("Symbol")
     elif(choice == 'Letter' and chosenLetter < number_of_letters):
        passwordString+= random.choice(letters)
        chosenLetter+=1
        break
     elif choice == 'Letter' and chosenLetter == number_of_letters:
        possible_choices.remove("Letter")
     if(choice == 'Number' and chosenNumber < number_of_numbers):
        passwordString += str(random.randint(0,11))
        chosenNumber+=1
        break
     elif choice == 'Number' and chosenNumber == number_of_numbers:
        possible_choices.remove("Number")
print(passwordString+ " is your new password.")