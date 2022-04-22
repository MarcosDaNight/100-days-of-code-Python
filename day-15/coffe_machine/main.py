from art import logo, layout
from data import MENU, resources, coins
from os import system

def client_wallet(quarters, dimes, nickels, pennies):
    """Function for a calculating how many coins the client have a insert"""
    total = (coins['quarter'] * quarters) + (coins['dime'] * dimes) + \
        (coins['nickel'] * nickels) + (coins['penny'] * pennies)
    return total


def verify_cost(wallet, cost, chose):
    """Function for a verify user wallet when they buy a coffe"""
    change = wallet - cost
    if change >= 0:
        if change == 0:
            print("Don't have a change. Thanks for buying.")
            print(f"Here is your {chose}☕. Enjoy!")
            return change
        else:
            print("Here is your change {:.2f}".format(change))
            print(f"Here is your {chose}☕. Enjoy!")
            return change
    else:
        print("Sorry that's not enough money. Money refunded.")
        return change

def checking_resources(resources, ingredients):
    """Cheking if resources are sufficiente before the buy"""
    for r in resources:
        if r in ingredients:
            if resources[r] >= ingredients[r]:
                return True
            else:
                return False


def calculating_resources(resources, ingredients):
    """Atualize resources after buy"""
    if checking_resources(resources, ingredients):
        for r in ingredients:
            resources[r] -= ingredients[r]  
    return resources


def main():
    print(layout)
    print(logo)
    resources_ramaning = resources
    while True:
       
        chose = input("\nWhat would you like? (espresso/latte/cappuccino): ")

        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        wallet = client_wallet(quarters, dimes, nickels, pennies,)


        coffe = MENU[chose]
        verify_cost(wallet, coffe['cost'], chose)


        print(checking_resources(resources, coffe['ingredients']))
        if checking_resources(resources, coffe['ingredients']):
            resources_ramaning = calculating_resources(resources_ramaning, coffe['ingredients'])
            
        else:
            print('Not enought resources sufficienty, try other order.')
            


main()