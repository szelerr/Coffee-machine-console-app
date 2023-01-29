from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneyMachine = MoneyMachine()
coffeMaker = CoffeeMaker()
menu = Menu()

while True:    
    print(menu.get_items())
    choice = input("What would you like? ")

    if choice == "off":
        print("Shutting down...")
        break
    elif choice == "report":
        coffeMaker.report()
        moneyMachine.report()
    else:
        order = menu.find_drink(choice)
        if coffeMaker.is_resource_sufficient(order) and moneyMachine.make_payment(order.cost):
                coffeMaker.make_coffee(order)