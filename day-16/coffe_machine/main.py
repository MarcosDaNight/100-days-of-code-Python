from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    money_machine = MoneyMachine()
    menu = Menu()
    coffee_maker = CoffeeMaker()

    is_one = True

    while is_one:
        options = menu.get_items()

        choice = input(f"What would you like? ({options}): ")

        if choice == "off":
            is_one = False

        elif choice == "report":
            coffee_maker.report()
            money_machine.report()

        else:
            drink = menu.find_drink(choice)

            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

main()