catNames = []

def printCatNames(catList):
    for i in range(len(catList)):
        print(str(i+1) +'. ' + catList[i])

while True:
    print('Enter the name of cat number ' + str(len(catNames) + 1) + 
        ' or enter to stop')

    cat_name_input = input()
    if(cat_name_input == None or cat_name_input == ''):
        break
    else:
        catNames = catNames + [cat_name_input] # Adds to the list and concats

if len(catNames) == 0:
    print('You have no cats :(')
elif len(catNames) == 1:
    print("You only have 1 cat")
else:
    print("You have " + str(len(catNames)) + ' cat')

printCatNames(catNames)
