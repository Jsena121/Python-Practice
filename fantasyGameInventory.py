stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def displayInventory(inventory):
    print ("Inventory:")
    itemTotal = 0
    for k, v in inventory.items():
        print (str(v) + ' ' + str(k))
        itemTotal += v
    print("total number of items: " + str(itemTotal))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item,0)
        inventory[item]+=1
        #print(inventory)
    return inventory
    #for k, v in inventory.items():   error bc dictionary size changes
        #for item in addedItems:
           # inventory.setdefault(item,0)
           # inventory[item]+=1

displayInventory (stuff)

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

stuff = addToInventory (stuff, dragonLoot)
displayInventory(stuff)
