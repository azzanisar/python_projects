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

# We can use the profit variable to modify the money used to  make the coffee
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: Check resources sufficient
def is_resource_sufficient(order_ingredients):
   """
   Returns True when order can be made and False if ingredients are insufficent
   """
   for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
           print(f"Sorry there is not enough {item}.")
           return False
   return True
        # water is the item for example and we compare how much is required from resources

#TODO: Process coins

def process_coins():
    """
    Returns total calculated from coins inserted
    """
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

#TODO: Check transaction successful

def check_transaction(payment_inserted, drink_cost):
    """
    Return True when payment is accepted or False if money is insufficient
    """
    if payment_inserted >= drink_cost:
        change = round(payment_inserted - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

#TODO: Make Coffee

def make_coffee(drink_name, order_ingredients):
    """
    Deduct the required ingredients from the resources
    """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕")


is_on = True
while is_on:
    #TODO: Prompt user by asking
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice == "off":
        is_on = False # off is the secret word to turn off the machine

    #TODO: Print report
    elif user_choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} ml")
        print(f"Money: ${profit}")

    else: #machine is on
        drink = MENU[user_choice] #so we store each coffee's details as variable
        # if resources are sufficient for making the drink then proceed to next step
        # TODO: Process coins
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins() #we insert payment
            if check_transaction(payment, drink["cost"]):
                #if we have inserted payment and resources are sufficient
                make_coffee(user_choice, drink["ingredients"])







