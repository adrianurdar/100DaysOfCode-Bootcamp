# Coffee Machine OOP

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys


def main():
    # Create a Coffee Maker object
    coffee_maker = CoffeeMaker()

    # Create a menu object
    menu = Menu()

    # Create the money machine object
    money_machine = MoneyMachine()

    # Turn machine on
    while True:
        input_ok = False
        while not input_ok:
            # Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
            product = input(f"What would you like? ({menu.get_items()}): ").lower()

            # Turn off the Coffee Machine by entering “off” to the prompt.
            if product == "off":
                sys.exit()

            # Print report.
            elif product == "report":
                coffee_maker.report()
                money_machine.report()

            else:
                drink = menu.find_drink(product)
                input_ok = True

        # Check resources sufficient?
        if coffee_maker.is_resource_sufficient(drink):

            # Check transaction successful?
            if money_machine.make_payment(drink.cost):

                # Make Coffee.
                coffee_maker.make_coffee(drink)


if __name__ == "__main__":
    main()
