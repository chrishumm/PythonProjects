from multiprocessing.connection import wait
import pyinputplus as pyin


water = 100
milk = 100
coffee = 100
money = 1.00

FIFTY_PENCE = 0.50
ONE_POUND = 1.00
TWENTY_PENCE = 0.20
FIVE_PENCE = 0.05
TWO_PENCE = 0.02

ESPRESSO_PRICE = 2.50
ESPRESSO_MILK = 12.00
ESPRESSO_WATER = 5.00
ESPRESSO_COFFEE = 80.00

LATTE_PRICE = 1.25
LATTE_MILK = 60.00
LATTE_WATER = 10.00
LATTE_COFFEE = 60.00

CAPPUCCINO_PRICE = 3.00
CAPPUCCINO_MILK = 50.00
CAPPUCCINO_WATER = 25.00
CAPPUCCINO_COFFEE = 70.00

def report():
    print(f"Current Water: {water}ml\nCurrent Milk: {milk}ml\nCurrent Coffee: {coffee}g\nCurrent Money: {money}\n")

def checkResources(coffee_type):
    if(coffee_type == "espresso"):
        if(milk < ESPRESSO_MILK or coffee < ESPRESSO_COFFEE or water < ESPRESSO_WATER):
            return False
        else:
            return True
    elif coffee_type == "latte":
        if(milk < LATTE_MILK or coffee < LATTE_COFFEE or water < LATTE_WATER):
            return False
        else:
            return True
    elif coffee_type == "cappuccino":
        if milk < CAPPUCCINO_MILK or coffee < CAPPUCCINO_COFFEE or water < CAPPUCCINO_WATER:
            return False
        else:
            return True

def checkPrice(coffee):
    if(coffee == "espresso"):
        if(money < ESPRESSO_PRICE):
            print(f"You don't have enough money. You need to add ${ESPRESSO_PRICE - money}")
            return False
        else:
            return True
    elif(coffee == "latte"):
        if(money < LATTE_PRICE):
            print(f"You don't have enough money. You need to add ${LATTE_PRICE - money}")
            return False
        else:
            return True
    elif(coffee == "cappuccino"):
        if(money < CAPPUCCINO_PRICE):
            print(f"You don't have enough money. You need to add ${CAPPUCCINO_PRICE - money}")
            return False
        else:
            return True
    else:
            return False

def returnChange():
    global money
    money = 0.0

def menu():
    input = pyin.inputMenu(["Order","Report","Return Change","Turn Off"], f"You have ${money}\nWhat would you like?\n",numbered=True)
    if(input == "Order"):
        orderCoffee()
    elif(input == "Report"):
        report()
        menu()
    elif input == "Return Change":
        returnChange()
        menu()
    elif input == "Turn Off":
        return

def inputAmount():
    input = pyin.inputInt("Please enter amount of coins\n")
    return input

def addMoney():
    global money
    input = pyin.inputMenu(["Fifty Pence","Twenty Pence","One Pound", "Five Pence", "Two Pence", "Exit"], f"You have ${money}\nPlease enter coins\n",numbered=True)
    if(input == "Fifty Pence"):
        money += FIFTY_PENCE*inputAmount()
    elif(input == "Twenty Pence"):
        money += TWENTY_PENCE*inputAmount()
    elif(input == "One Pound"):
        money += ONE_POUND*inputAmount()
    elif(input == "Five Pence"):
        money += FIVE_PENCE*inputAmount()
    elif(input == "Two Pence"):
        money += TWO_PENCE*inputAmount()
    elif(input == "Exit"):
        return True
    else:
        money += 0

    return False

def deductResources(coffee_type):
    global water
    global milk
    global coffee
    global money
    if(coffee_type == "espresso"):
        money -= ESPRESSO_PRICE
        milk -= ESPRESSO_MILK
        coffee -= ESPRESSO_COFFEE
        water -= ESPRESSO_WATER
    elif coffee_type == "latte":
        money -= LATTE_PRICE
        milk -= LATTE_MILK
        coffee -= LATTE_COFFEE
        water -= LATTE_WATER
    elif coffee_type == "cappuccino":
        money -= CAPPUCCINO_PRICE
        milk -= CAPPUCCINO_MILK
        coffee -= CAPPUCCINO_COFFEE
        water -= CAPPUCCINO_WATER
    else:
        print("Error")
def orderCoffee():
    coffee_type = pyin.inputMenu(["espresso","latte","cappuccino"], f"You have ${money}\nWhat would you like?\n",numbered=True)
    if checkPrice(coffee_type) == False:
       answer = pyin.inputYesNo("Do you want to add more money? Enter Yes or No: ",)
       if(answer == "yes"):
            while True:
                if addMoney() == True:
                    break
            orderCoffee()
       else:
            menu()
    else:
            if checkResources(coffee_type) == False:
                print("NOT ENOUGH RESOURCES")
                menu()
            else:
                deductResources(coffee_type)
                print("Enjoy your " + coffee_type)
                menu()

menu()


