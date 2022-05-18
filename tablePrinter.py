table = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

colsWidths = [0]*len(table) #width of column

for i in range(len(table)):
        colsWidths[i] = len(max(table[i], key = len)) # 
        # colsWidths = [8,5,5]

columns = len(table[0]) # 4
rows = len(table) # 3 items

for print_columns in range(columns):
        for print_rows in range(rows):
            print(table[print_rows][print_columns].rjust(colsWidths[print_rows], " "), end = "  ")
        print()