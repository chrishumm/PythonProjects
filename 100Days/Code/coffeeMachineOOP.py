from prettytable import PrettyTable
import pyinputplus as pyin
class Coffee:
    def __init__(self) -> None:
        self.milk = 0.0
        self.water = 0.0
        self.coffee = 0.0
        self.cost = 0.0

    def getMilk(self):
        return self.milk

    def getWater(self):
        return self.water

    def getCoffee(self):
        return self.coffee

    def getCost(self):
        return self.cost

class Latte(Coffee):
    def __init__(self) -> None:
        super().__init__()
        self.milk = 10.0
        self.water = 20.0
        self.coffee = 30.0
        self.cost = 10.00

class Cappucinno(Coffee):
    def __init__(self) -> None:
        super().__init__()
        self.milk = 40.0
        self.water = 22.0
        self.coffee = 50.0
        self.cost = 25.00

class CoffeeFactory():
    def __init__(self)-> None :
        print("")

    def CreateCoffeeObject(self, coffee_name):
        if coffee_name == "Latte":
            coffee = Latte()
            return coffee
        elif coffee_name == "Cappucinno":
            coffee = Cappucinno()
            return coffee

class Resources:
    def __init__(self) -> None:
        self.milk = 100.0
        self.water = 100.0
        self.coffee = 100.0
        self.money = 0.0
        pass

    def getMilk(self):
        return self.milk

    def deductMilk(self, amount):
        if self.milk - amount  < 0:
            return False
        else:
            return True

    def getWater(self):
        return self.water

    def deductWater(self, amount):
        if self.water - amount < 0:
            return False
        else:
            return True

    def getCoffee(self):
        return self.coffee

    def deductCoffee(self, amount):
        if self.coffee - amount < 0:
            return False
        else:
            return True

    def getMoney(self):
        return self.money

    def addMoney(self, amount):
        self.money += amount

    def deductMoney(self, amount):
        if self.money - amount < 0:
            return False
        else:
            return True

    def deductResources(self,coffee_amount,milk_amount,water_amount,money_amount):
        self.coffee -= coffee_amount
        self.money -= money_amount
        self.water -= water_amount
        self.milk -= milk_amount


class CoffeeMachine:
    def __init__(self) -> None:
        self.resources  = Resources()
        self.moneyMachine = MoneyMachine(self.resources)

        self.isOn = True
        pass

    def printResources(self):
        resourceTable = PrettyTable()
        resourceTable.add_column("Resource",
        ["Milk", "Money", "Coffee","Water"])
        resourceTable.add_column("Amount",
        [self.resources.getMilk(),self.resources.getMoney(),self.resources.getCoffee(),self.resources.getWater()])
        resourceTable.align = "l"
        print(resourceTable)

    def makeCoffee(self,new_coffee : Coffee):
        if self.resources.deductCoffee(new_coffee.getCoffee()) == False:
            print("NOT ENOUGH COFFEE")
        elif self.resources.deductMilk(new_coffee.getMilk()) == False:
            print("NOT ENOUGH MILK")
        elif self.resources.deductWater(new_coffee.getWater()) == False:
            print("NOT ENOUGH WATER")
        elif self.resources.deductMoney(new_coffee.getCost()) == False:
            print("NOT ENOUGH MONEY")
            if pyin.inputYesNo("Do you want to add more money?") == "yes":
                self.moneyMachine.addCoins()
        else:
            self.resources.deductResources(new_coffee.getCoffee(),new_coffee.getMilk(),new_coffee.getWater(),new_coffee.getCost())
            print("Enjoy your drink!")

class MoneyMachine():
    def __init__(self, resources) -> None:
        self.machineResources = resources
        self.CURRENCY = "$"
        self.COINS = {"Ten Pence" : 0.10,"Twenty Pence" : 0.20,"Fifty Pence" : 0.50,"One Pound" : 1.00}
        pass

    def addCoins(self):
        coin_type = pyin.inputMenu(["Ten Pence", "Twenty Pence", "Fifty Pence", "One Pound"], "What coins do you want to add?\n", numbered=True)
        coin_amount = pyin.inputInt("How many?")
        total_amount = self.COINS[coin_type] * coin_amount
        self.machineResources.addMoney(total_amount)

class Menu():
    def __init__(self) -> None:
        self.coffeeMachine = CoffeeMachine()
        self.menuItem = ["Print Report", "Make Coffee", "Turn Off", "Add Money"]
        self.coffeeItem = ["Latte", "Cappucinno"]
        self.coffeeFactory = CoffeeFactory()
        pass

    def displayMenu(self):
        response = pyin.inputMenu(self.menuItem,"What do you want to do today?\n", lettered=True)
        if response == "Print Report":
            self.coffeeMachine.printResources()
        elif response == "Make Coffee":
            response = pyin.inputMenu(self.coffeeItem,"What do you want to drink today?\n2",lettered=True)
            coffee = self.coffeeFactory.CreateCoffeeObject(response)
            self.coffeeMachine.makeCoffee(coffee)
        elif response == "Turn Off":
            return 0 
        elif response == "Add Money":
            self.coffeeMachine.moneyMachine.addCoins()
        self.displayMenu()


new_menu = Menu()
new_menu.displayMenu()