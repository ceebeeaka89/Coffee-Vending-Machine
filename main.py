MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
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

coinbase = {
   "nickel":0.05 ,
   "penny": 0.01,
   "dime": 0.10,
   "quarter": 0.25,
}

machine_is_on = True

#TODO4. Check resources sufficient?
def check_resource(drink_name): 
    # Extract the required ingredients from the MENU for the given drink
    required_ingredients = MENU[drink_name]['ingredients']
    
    # Debug print to confirm what we're checking
    print(f"Checking resources for {drink_name}")
    print(f"Required Ingredients: {required_ingredients}")
    print(f"Available Resources: {resources}")
    
    # Check each resource
    for ingredient, amount_needed in required_ingredients.items():
        available_amount = resources.get(ingredient, 0)
        #print(f"Checking {ingredient}: required {amount_needed}, available {available_amount}")
        if available_amount < amount_needed:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    
    # If all resources are sufficient
    return True


#TODO7. Make Coffee.
    # after previous purchase subtract from current resource
def Make_coffee(drink_name):
  current_order = MENU[drink_name]['ingredients']
  #for loop that iterates through the ingretiates and for each ingrediate take away from resource
  for ingredient, amount in current_order.items():
     resources[ingredient] -= amount

  return resources

#TODO5. Process coins.
def process_coins(drink_name):

    required_price = MENU[drink_name]['cost']
    correct_coins = False

    while not correct_coins:
      quantities = {}

      for coin in coinbase.keys():
        quantity = float(input(f"How many {coin}s?:"))
        quantities[coin] = quantity
      
      total_paid = 0

      for coin,value in coinbase.items():
        coin_total = value * quantities[coin]
        total_paid += coin_total
        print(f"The value inserted of {quantities[coin]} {coin}(s) is ${coin_total:.2f}")

      print(f"\nThe total inserted is ${total_paid:.2f}")     
      
      if required_price == total_paid:
          print("Correct amount")
          correct_coins = True
          return total_paid
      elif required_price > total_paid: 
          print('Sorry not enough money. Money refunded ')
      else: 
          change = total_paid - required_price
          print (f'Please takes your change of ${change:.2f}.')
          correct_coins = True
          return total_paid
      

while machine_is_on:
#TODO1. Prompt user by asking “​What would you like? (espresso/latte/cappuccino):”​
  User_request = input('what would you like to drink? espresso/latte/cappuccino: ').lower()
  if User_request == 'espresso': 
    if check_resource(User_request) == True:
       process_coins(User_request)
       Make_coffee(User_request)
       print('making espresso...')
  elif User_request == 'latte':
    if check_resource(User_request) == True:
      process_coins(User_request)
      Make_coffee(User_request)
      print('making a latte...') 
  elif User_request == 'cappuccino':
    if check_resource(User_request) == True:
      process_coins(User_request)
      Make_coffee(User_request)
      print('making a cappuccino...') 

#TODO2. Turn off the Coffee Machine by entering “​off”​ to the prompt
  elif User_request == 'off':
      print("turning off machine")
      machine_is_on = False

#TODO3. Print report.
  elif User_request == 'report':
     print(f' Water: {resources['water']}ml \n Milk: {resources["milk"]}ml \n Coffee: {resources['coffee']}ml')


#TODO6. Check transaction successful?

# Newline
