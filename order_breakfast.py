import time

# print_pause() displays message to user and pause 'x' second(s) after each line  
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1.5)

# Intro() displays the introduction of the order_breakfast program
def intro():
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")

# Check validity of the user's input
def valid_input(prompt, optionA, optionB):
    while True:        
        response = input(prompt).lower() 
        if optionA in response: 
            break      
        elif optionB in response:
            break
        #Reject user's input besides the passed parameters' values  
        else:
            print_pause("Sorry, I don't understand.\n")
    return response

# Get user's order
def order():
    opt1 = 'waffles'
    opt2 = 'pancakes'
    ask = valid_input(f"Please place your order. Would you like {opt1} or {opt2}?\n", opt1, opt2)
    if opt1 in ask:
        print_pause(f"{opt1.capitalize()} it is!")
    elif opt2 in ask:
        print_pause(f"{opt2.capitalize()} it is!")
    print_pause("Your order will be ready shortly.")

# Check if the user wants to order again
def order_again():
    optA = 'yes'
    optB = 'no'
    while True:
        prompt = valid_input(f"Would you like to place another order? Please say '{optA}' or '{optB}'.\n", optA, optB)
        if optA in prompt:
            print_pause("Very good, I'm happy to take another order.")
            order()
        elif optB in prompt:
            print_pause('OK, goodbye!')
            break

# Main function to get the program started
def order_breakfast():
    intro()
    order()
    order_again()
    print('You may exit the program')

# Start the program
order_breakfast()
