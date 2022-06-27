import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

print_pause("Hello! I am Bob, the Breakfast Bot.")
print_pause("Today we have two breakfasts available.")
print_pause("The first is waffles with strawberries and whipped cream.")
print_pause("The second is sweet potato pancakes with butter and syrup.")

def order():
    while True:
        response = input("Please place your order. Would you like waffles or pancakes?\n").lower()
        if "waffles" in response:
            print("Waffles it is!")
            time.sleep(2)
            break
        elif "pancakes" in response:
            print("Pancakes it is!")
            time.sleep(2)
            break
        else:
            print("Sorry, I don't understand.")
            time.sleep(2)
    print("Your order will be ready shortly.")
    time.sleep(2)

def order_again():
    while True:
        again= input("Would you like to place another order? Please say 'yes' or 'no'.").lower()
        if ('yes'or 'y') in again:
            time.sleep(2)
            print("Very good, I'm happy to take another order.")
            order()
        elif ('no' or 'n') in again:
            time.sleep(2)
            print('OK, goodbye!')
            break
        else:
            print("Sorry, I don't understand.")

print_pause()
order()
order_again()  
print('You may exit this page')
