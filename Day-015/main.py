import sys

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def turn_off():
    """
    Turn off Coffee Machine by entering "off" to the prompt. For maintainers of the coffee machine, they can use “off”
     as the secret word to turn off the machine. Your code should end execution when this happens.
    """
    return sys.exit()


def report():
    """
    Print report.
     When the user enters “report” to the prompt, a report should be generated that shows
     the current resource values.
     e.g.
     Water: 100ml
     Milk: 50ml
     Coffee: 76g
     Money: $2.5
    """
    print(f"💧 Water: {resources['water']}ml")
    print(f"🥛 Milk: {resources['milk']}ml")
    print(f"☕️ Coffee: {resources['coffee']}g")
    try:
        print("💵 Money: ${:.2f}".format(resources['money']))
    except KeyError:
        pass


def check_resource(product):
    """
    Check resources sufficient?
    When the user chooses a drink, the program should check if there are enough
     resources to make that drink.
    E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
     not continue to make the drink but print: “ Sorry there is not enough water. ”
     The same should happen if another resource is depleted, e.g. milk or coffee.
    """
    if resources['water'] < MENU[product]['ingredients']['water']:
        print("Sorry. Not enough water.")
        return False
    elif resources['coffee'] < MENU[product]['ingredients']['coffee']:
        print("Sorry. Not enough coffee.")
        return False
    elif 'milk' in MENU[product]['ingredients'].keys() and resources['milk'] < MENU[product]['ingredients']['milk']:
        print("Sorry. Not enough milk.")
        return False
    else:
        return True


def process_coins():
    """
    Process coins.
    If there are sufficient resources to make the drink selected, then the program should
     prompt the user to insert coins.
    Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    Calculate the monetary value of the coins inserted.
     E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
    """
    print("Please insert coins.")
    input_ok = False
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    while not input_ok:
        try:
            quarters = float(input("    🪙 How many quarters? "))
            input_ok = True
        except ValueError:
            pass
    input_ok = False
    while not input_ok:
        try:
            dimes = float(input("    🪙 How many dimes? "))
            input_ok = True
        except ValueError:
            pass
    input_ok = False
    while not input_ok:
        try:
            nickels = float(input("    🪙 How many nickels? "))
            input_ok = True
        except ValueError:
            pass
    input_ok = False
    while not input_ok:
        try:
            pennies = float(input("    🪙 How many pennies? "))
            input_ok = True
        except ValueError:
            pass
    # quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total


def check_transaction(total, product):
    """
    Check transaction successful?
    a. Check that the user has inserted enough money to purchase the drink they selected.
     E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
     program should say “ Sorry that's not enough money. Money refunded. ”.
    b. But if the user has inserted enough money, then the cost of the drink gets added to the
     machine as the profit and this will be reflected the next time “report” is triggered.
     E.g.
     Water: 100ml
     Milk: 50ml
     Coffee: 76g
     Money: $2.5
    c. If the user has inserted too much money, the machine should offer change.
     E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
    """
    if total < MENU[product]['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        if 'money' in resources.keys():
            resources['money'] += total
        else:
            resources['money'] = total
        change = total - MENU[product]['cost']
        if change > 0:
            print("💵 Here is ${:.2f} dollars in change.".format(change))
        return True


def make_coffee(product):
    """
    Make Coffee.
    If the transaction is successful and there are enough resources to make the drink the user selected, then the
     ingredients to make the drink should be deducted from the coffee machine resources.
    E.g. report before purchasing latte:
     Water: 300ml
     Milk: 200ml
     Coffee: 100g
     Money: $0
    Report after purchasing latte:
     Water: 100ml
     Milk: 50ml
     Coffee: 76g
     Money: $2.5
    Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of
     drink.
    """
    resources['water'] -= MENU[product]['ingredients']['water']
    resources['coffee'] -= MENU[product]['ingredients']['coffee']
    if 'milk' in MENU[product]['ingredients'].keys():
        resources['milk'] -= MENU[product]['ingredients']['milk']
    print(f"Here is your {product}. Enjoy!")


def main():
    while True:
        # 1. Prompt user by asking "What would you like? (espresso, cappuccino, latte): "
        # 1.1. Check the user's input what to do next
        # 1.2. The prompt should show each time the action is completed. E.g. once drink is dispensed, the user should
        #  be prompted again
        products = ["espresso", "latte", "cappuccino", "off", "report"]
        input_ok = False
        product = 0
        while not input_ok:
            product = input("What ☕ would you like? (espresso/latte/cappuccino): ").lower()
            if product in products:
                input_ok = True

        # Turn off Coffee Machine by entering "off" to the prompt
        if product == "off":
            turn_off()

        # Print report.
        elif product == "report":
            report()

        else:

            # Check resources sufficient?
            if check_resource(product):

                # Process coins.
                total = process_coins()

                # Check transaction successful?
                if check_transaction(total, product):

                    # Make Coffee.
                    make_coffee(product)


if __name__ == "__main__":
    main()
