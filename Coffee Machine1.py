water = int(input('Write how many ml of water the coffee machine has in it? \n'))
milk = int(input('Write how many ml of milk the coffee machine has in it?: \n'))
coffee_beans = int(input('Write how many grams of coffee beans the coffee machine has in it? \n'))
disposable_cups = int(input('Write how many disposable_cups the coffee machine has in it? \n'))
money = int(input('Write how  much money the coffee machine has in it? \n'))
class CoffeeMachine:
    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water = water
        self. milk =  milk
        self.coffee_beans = coffee_beans 
        selfdisposable_cups = disposable_cups
        self.money = money

    def buy_coffee(self):
        print()
        coffee = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, break - to main menu:\n')
        water_espresso = 250
        coffee_beans_espresso = 16
        money_espresso = 4
        water_latte = 350
        milk_latte = 75
        coffee_beans_latte = 20
        money_latte = 7
        water_cappuccino = 200
        milk_cappuccino = 100
        coffee_beans_cappuccino = 12
        money_cappuccino = 6
        if coffee == '1':
            global water
            global coffee_beans
            if water < water_espresso:
                print("Sorry, not enough water!")
                print()
               
            elif coffee_beans < coffee_beans_espresso:
                print("Sorry, not enough cofee_beans!")
                print()   
            else:
                water -= water_espresso
                coffee_beans -= coffee_beans_espresso 
                global disposable_cups
                disposable_cups -= 1
                global  money
                money += money_espresso
                print("I have enough resources, making you a coffee!")
                print()
        elif coffee == '2':
            global milk
            if water < water_latte:
                print("Sorry, not enough water!")
                print()
            elif coffee_beans < coffee_beans_latte:
                print("Sorry, not enough cofee_beans!")
                print()
            elif   milk < milk_latte:
                print("Sorry, not enough milk!")
                print()
            else:
                water -= water_latte   
                milk -= milk_latte
                coffee_beans -= coffee_beans_latte
                disposable_cups -= 1
                money += money_latte
                print("I have enough resources, making you a coffee!")
                print()
        elif coffee == '3':
             if water < water_cappuccino:
                print("Sorry, not enough water!")
                print()
             elif coffee_beans < coffee_beans_cappuccino:
                print("Sorry, not enough cofee_beans!")
                print()
             elif   milk < milk_cappuccino:
                print("Sorry, not enough milk!")
                print()
             else:
                water -= water_cappuccino  
                milk -= milk_cappuccino
                coffee_beans -= coffee_beans_cappuccino 
                disposable_cups -= 1
                money += money_cappuccino
                print("I have enough resources, making you a coffee!")
                print()
                
    def fill_coffee(self):
        water_fill = int(input('Write how many ml of water do you want to add: \n'))
        milk_fill = int(input('Write how many ml of milk do you want to add: \n'))
        coffee_beans_fill = int(input('Write how many grams of coffee beans do you want to add: \n'))
        disposable_cups_fill = int(input('Write how many disposable_cups do you want to add: \n'))
        global water
        water += water_fill
        global milk
        milk += milk_fill
        global coffee_beans
        coffee_beans += coffee_beans_fill
        global disposable_cups
        disposable_cups += disposable_cups_fill
        print()

    def money_coffee(self):
        global  money
        print()
        print('I gave you $%d' % money)
        money = money - money
        print()
    def remaining_coffee(self):
        print()
        print('The coffee machine has:')
        print('%d of water' % water)
        print('%d of milk' % milk)
        print('%d of coffee_beans' % coffee_beans)
        print('%d of disposable cups' % disposable_cups)
        print('$%d of money' % money)
        print()

coffee = CoffeeMachine(400, 540, 120, 9, 550)      
i = True
while  i is True:
    action = input('Write action (buy, fill, take, remaining, exit): \n')

    if action == 'buy':
       coffee.buy_coffee()
    elif action == 'fill':
        coffee.fill_coffee()
    elif action == 'remaining':
        coffee.remaining_coffee()
    elif action == 'take':
        coffee.money_coffee()
    else:
        print()
        i = False

               

