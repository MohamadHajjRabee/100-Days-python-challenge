from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


turn_machine_off = False
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while not turn_machine_off:
    order_name = input(f"What would you like? ({Menu().get_items()}):")
    if order_name == "off":
        turn_machine_off = True
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        order = Menu().find_drink(order_name)

        if coffee_maker.is_resource_sufficient(order):

            take_money = money_machine.make_payment(order.cost)

            if take_money:
                coffee_maker.make_coffee(order)
