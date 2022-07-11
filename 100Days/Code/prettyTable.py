from prettytable import PrettyTable


newTable = PrettyTable()

newTable.add_column("Pokemon Name",
["Pikachu","Squirtle","Charmander"])
newTable.add_column("Type", 
["Eletric", "Water", "Fire"])
newTable.align = "l"
print(newTable)