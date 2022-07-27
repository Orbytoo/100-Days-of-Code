from os import system

system('cls')


"""
    Coffe Machine Program // Programa Máquina de Café 
"""

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

machine_profit = 0 # lucro da maquina
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}



def check_resources_sufficient(info_menu):
    """Retorna True se tiver recursos suficiente para fazer o café, caso contrário, False."""
    for item in info_menu:
        if info_menu[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def insert_coins():
    """Retorna os coins após serem adicionandos, serão usados para compras."""
    print("Please insert coins.")
    tot = int(input("how many quarters?: ")) * 0.25
    tot += int(input("how many dimes?: ")) * 0.10
    tot += int(input("how many nickles?: ")) * 0.05
    tot += int(input("how many pennies?: ")) * 0.01
    
    return tot


def transaction_successful(your_coins, coffee_price):
    """Return True caso o usuário tenha coins suficiente para comprar o café, caso contrário, False."""
    if your_coins > coffee_price:
        global machine_profit
        machine_profit += coffee_price
        print(f"Here is ${round(your_coins - coffee_price, 2)} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(info_menu, choice):
    for item in info_menu:
        resources[item] -= info_menu[item]

    print(f"Here is your {choice} ☕. Enjoy!")
    

coffe_maker_on = True # cafeteira ligada

while coffe_maker_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        coffe_maker_on = False
    elif choice == 'report':  
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${machine_profit}")
    else:
        master = MENU[choice]
        result = check_resources_sufficient(master["ingredients"])
        if result == True:
            your_coins = insert_coins()
            if transaction_successful(your_coins, master["cost"]):
                make_coffee(master["ingredients"], choice)


