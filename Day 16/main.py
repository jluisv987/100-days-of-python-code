from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_make = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
menu = Menu()
print("Welcome to the coffee machine")

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}:")
    if choice == "off":
        is_on = False
    elif choice =="report":
        money_machine.report()
        coffee_make.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_make.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_make.make_coffee(drink)

