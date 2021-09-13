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


def check_resources(order):
    for item in order['ingredients']:
        if order['ingredients'][item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False

        return True


def calculate_money(user_order, order, quarters, dimes, nickles, pennies):

    cost = 0.25 * quarters + 0.1 * dimes + 0.05 * nickles + 0.01 * pennies
    if cost < order['cost']:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    else:
        money_change = round(cost - order['cost'], 2)
        print(f"Here is ${money_change} in change")
        print(f"Here is your {user_order} ☕️. Enjoy!")
        for item in order['ingredients']:
            resources[item] -= order['ingredients'][item]
        return (order['cost'])


Money = 0

turn_machine_off = False
while not turn_machine_off:
    user_order = input("  What would you like? (espresso/latte/cappuccino): ")

    if user_order in MENU:
        order = MENU[user_order]
        if check_resources(order):
            print("Please insert coins.")
            hw_quarters = int(input("How many quarters?: "))
            hw_dimes = int(input("How many dimes?: "))
            hw_nickles = int(input("How many nickles?: "))
            hw_pennies = int(input("How many pennies?: "))
            Money += calculate_money(user_order, order, hw_quarters,
                                     hw_dimes, hw_nickles, hw_pennies)

    elif user_order == "report":

        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${Money}")
    elif user_order == "off":
        turn_machine_off = True
