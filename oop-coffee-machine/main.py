from coffee_machine import MENU, resources

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01

profit = 0


def print_resources():
    """Prints the current profit and remaining resources"""
    print(f"Water: {resources['water']}mL")
    print(f"Milk: {resources['milk']}mL")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def check_resources(user_choice):
    """Checks if there are sufficient ingredients."""
    is_check = True
    water1 = MENU[user_choice]['ingredients']['water']
    water2 = resources['water']

    coffee1 = MENU[user_choice]['ingredients']['coffee']
    coffee2 = resources['coffee']

    if water2 - water1 < 0:
        print("Sorry, there's not enough water.")
        is_check = False
    if coffee2 - coffee1 < 0:
        print("Sorry, there's not enough coffee.")
        is_check = False
    if user_choice == 'latte' or user_choice == 'cappuccino':
        milk1 = MENU[user_choice]['ingredients']['milk']
        milk2 = resources['milk']
        if milk2 - milk1 < 0:
            print("Sorry, there's not enough milk.")
            is_check = False
    return is_check


def process_coins(user_choice):
    """Calculates your change. If amount given is insufficient, money is refunded."""
    print("Please insert coins.")
    quarter_amt = int(input("How many quarters?: "))
    dime_amt = int(input("How many dimes?: "))
    nickle_amt = int(input("How many nickles?: "))
    penny_amt = int(input("How many pennies?: "))

    total_money = (quarter_amt * QUARTER) + (dime_amt * DIME)
    total_money += (nickle_amt * NICKLE) + (penny_amt * PENNY)
    coffee_cost = MENU[user_choice]['cost']
    change = total_money - coffee_cost
    if change < 0:
        print("Insufficient funds. Money refunded...")
        process_coins(user_choice)
    else:
        global profit
        profit += coffee_cost
        print(f'Your change is: ${round(change, 2)}')


def make_coffee(user_choice):
    """Updates the resources."""
    resources['water'] -= MENU[user_choice]['ingredients']['water']
    resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']
    if user_choice == 'latte' or user_choice == 'cappuccino':
        resources['milk'] -= MENU[user_choice]['ingredients']['milk']


def main():
    while 1:
        usr_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if usr_prompt == 'off':
            break
        elif usr_prompt == 'report':
            print_resources()
            continue
        if not check_resources(usr_prompt):
            continue

        print(f"Needed amount for {usr_prompt} is ${MENU[usr_prompt]['cost']}.")
        process_coins(usr_prompt)
        make_coffee(usr_prompt)
        print(f"Here is your {usr_prompt} ☕ Enjoy!")


if __name__ == "__main__":
    main()
