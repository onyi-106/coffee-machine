from menu import MENU, RESOURCES


# TODO Make a function to call the return the ingredients with the corresponding coffee

def ingredients(coffee_choice, coffee_ingredients):
    """
    coffee = name of the coffee (espresso/latte/cappuccino)
    ingredients = the substance (water/milk/coffee)
    """
    return MENU[coffee_choice]["ingredients"][coffee_ingredients]


def coffee_cost(coffee_choice):
    cost = MENU[coffee_choice]["cost"]
    return cost


# TODO Resources checking before making coffee
def is_sufficient():
    if water - ingredients(coffee_choice=COFFEE, coffee_ingredients="water") < 0:
        # Insufficient Resources
        print("Sorry there is not enough water.")
        return False
    # Espresso doesnt use milk, so: elif COFFEE != "espresso"....
    elif COFFEE != "espresso" and milk - ingredients(coffee_choice=COFFEE, coffee_ingredients="milk") < 0:
        # Insufficient Resources
        print("Sorry there is not enough milk.")
        return False
    elif coffee - ingredients(coffee_choice=COFFEE, coffee_ingredients="coffee") < 0:
        # Insufficient Resources
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def insert_money():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total_money


def report():
    report_format = f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money} "
    print(report_format)


water = RESOURCES["water"]
milk = RESOURCES["milk"]
coffee = RESOURCES["coffee"]
money = RESOURCES["money"]

# Machine Operation
machine_off = False
while not machine_off:
    COFFEE = input("What would you like? (espresso/latte/cappuccino): ")
    # TODO Make a turn off machine command
    if COFFEE == "off":
        machine_off = True
        print("Machine Off")
    # TODO Make a report command
    elif COFFEE == "report":
        report()

    # TODO The coffee machine should only work when there is sufficient resources and balance
    # Ask for coins if the resources are enough
    elif is_sufficient():
        print("Please insert coins")
        money_inserted = insert_money()
        if money_inserted >= coffee_cost(coffee_choice=COFFEE):
            change = money_inserted - coffee_cost(coffee_choice=COFFEE)
            print(f"Here's ${change} in change")
            print(f"Here's your {COFFEE}. Enjoy! :)")

            # After purchase mechanism
            # Water
            water = water - ingredients(coffee_choice=COFFEE, coffee_ingredients="water")
            # Coffee
            coffee = coffee - ingredients(coffee_choice=COFFEE, coffee_ingredients="coffee")
            if COFFEE != "espresso":
                # Milk
                milk = milk - ingredients(coffee_choice=COFFEE, coffee_ingredients="milk")
            # Money
            money += coffee_cost(coffee_choice=COFFEE)

        else:
            print("Sorry that's not enough money.")
