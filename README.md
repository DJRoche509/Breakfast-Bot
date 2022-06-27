# oder_breakfast
Simple Python program that takes user's input for ordering breakfast from a menu.

### Key features that this program is built with:
- To begin, messages are printed to the terminal for the user to see using the **print_pause()** function.

-  The breakfast menu option consist of two different items available for order: _waffles_ and _pancakes_. 

-  If user enters anything different than the given option, an error message is caught with the reply "**_Sorry, I don't understand_**" and displays same previous question to user. Otherwise, It displays a confirmation note stating what the user correctly chose.

- The program also responds appropriately (and to a certain extend) to bad inputs. If user says "yes, pancakes please". The bot understands and proceeds accordingly
    - The _in_ operator is used instead of an equality-check (_==_) in all three functions, **valid_input()**, **order()**, and **order_again()** to allow such flexibility

- The bot invites the user to order as many times as the user chooses to using a '_while_' loop in the **order_again()** function.


Several functions and variables were created in light of adopting a clean and reusable coding concept.
