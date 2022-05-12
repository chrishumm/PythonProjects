list_of_values = []

while True:
    print('Please (a)dd an item, (l)ist current items or (q)uit')
    menu_select = input()
    if(menu_select == 'a'):
        while True:
            print('Please write the name of the item or (q)uit')
            new_value = input()
            if new_value == '':
                print('Please enter a valid value')
            elif new_value == 'q':
                break
            else:
                list_of_values.append(new_value)
            
    elif(menu_select == 'l'):
        for index, list_value in enumerate(list_of_values):
            if index != len(list_of_values) - 1:
               print(list_value +', ', end='')
            else:
                print('and ' + list_value, end='')        
        print()