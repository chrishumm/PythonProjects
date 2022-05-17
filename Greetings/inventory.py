player_inventory  = {'Potion' : 1, 'Torch': 5, 'Coins' : 100}
monster_loot = {'Coins' : 100, 'Emerald': 1}

def outputInvent(player_inventory):
    print('Inventory:  ')
    totalItems = 0
    for k, v in player_inventory.items():
        totalItems = totalItems + player_inventory.get(k, 0)    
        print(k + ': ' + str(player_inventory.get(k, 0)))

    print("Total number of items: " + str(totalItems))
    return totalItems

def addToInventory(player_inventory, monster_loot):
    for k, i in monster_loot.items():
        if player_inventory.get(k, 0) == 0:
            player_inventory.setdefault(k, i)
        else:
         player_inventory[k] += i


outputInvent(player_inventory)

addToInventory(player_inventory, monster_loot)
print('Break')
outputInvent(player_inventory)
