menu={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccinno":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    },
}

resources ={
    "water":300,
    "milk":200,
    "coffee":100
}
def print_resources():
    print(f"Water:{resources['water']} ml")
    print(f"Milk:{resources['milk']} ml")
    print(f"Coffee:{resources['coffee']} gr")

def check_resources(drink):
    ing = drink["ingredients"]
    if ing["water"]<=resources["water"] and ing["coffee"]<=resources["coffee"]:
        if drink != 'espresso':
            if ing["milk"]<=resources["milk"]:
                resources["milk"] = resources["milk"] - ing["milk"]
                resources["water"] = resources["water"] - ing["water"]
                resources["coffee"] = resources["coffee"] - ing["coffee"]
                print("Available resources, the coffee was made")
                return 1
            else:
                print("Not enough resources")
                return 0
        else:
            resources["water"] = resources["water"] - ing["water"]
            resources["coffee"] = resources["coffee"] - ing["coffee"]
            print("Available resources, the coffee was made")
            return 1
    else:
        print("Not enough resources" )
        return 0
    

def check_money(drink,money):
    change = money
    if money>=drink["cost"]:
        if check_resources(drink):
            change = money - drink["cost"]       
        print("Your change is: $"+str(change))
    else:
        print("Error, there is not enough money to pay")

op=''
while op != 'exit':
    print("Welcome to the coffee machine")
    op = input("Please select a coffee, type 'espresso','latte', 'cappuccinno' or 'exit'\n")
    if op == 'exit':
        break
    drink = menu[op]
    dimes = float(input("How many dimes whould you insert in the machine\n"))
    nickles = float(input("How many nickles whould you insert in the machine\n"))
    pennies = float(input("How many pennies whould you insert in the machine\n"))
    dimes = 0.25*dimes
    nickles = 0.05*nickles
    pennies = 0.01*pennies
    print(drink)
    check_money(drink,nickles+dimes+pennies)
    print_resources()