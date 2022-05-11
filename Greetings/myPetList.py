import random

myPets = ['Woody', 'Bonnie', 'Bandit']

print('Enter the name of your pet')
pet_name = input()

if(pet_name not in myPets):
    print("You dont have a pet called " + pet_name)
else:
    print(pet_name + ' is your pet')


dog = ['Bandit', 'Border Collie', 10]
# Assigning multiple values in a list
name, breed, age = dog
print(name)
print(breed)
print(str(age))

#Enumerating through a list 
for index, item in enumerate(myPets):
    print('Pet number ' + str(index) + ' in your house ' + item)


#Chooses a random index in the list
print('Your favourite pet is ' + random.choice(myPets))
print(myPets) #prints the list unshuffled
random.shuffle(myPets)
print(myPets) #The list is shuffled

#Prints the number of the item in the list
print(myPets.index('Bonnie'))