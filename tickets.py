# Name: Aiden Higginbotham
# Prog Purpose: This program finds the cost of movie tickets
#   Price for one ticket: $10.99
#   Sales tax rate: 5.5%

import datetime

############    define global variables ###########
# define tax rate and prices
SALES_TAX_RATE = .055
PR_TICKET = 10.99

# define global variables
num_tickets = 0
subtotal = 0
sales_tax = 0
total = 0

############    define program functions ###########
def main():
    prompt_in = "\nWould you like to order again (Y or N) "
    goodbye_msg = "Thank you for your order. Enjoy your movie!"
    more_data = True
    
    while more_data:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input(prompt_in)
        if (yesno.upper() == "N"):
            more_data = False
            print(goodbye_msg)
            
def get_user_data():
    global num_tickets
    num_tickets = int(input("Number of movie tickets: "))

def perform_calculations():
    global subtotal, sales_tax, total
    subtotal = num_tickets * PR_TICKET
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

def display_results():
    line = '----------------------------------------------'
    currency = '8,.2f'
    date = str(datetime.datetime.now())
    title1 = '**** CINEMA HOUSE MOVIES ****'
    title2 = 'Your neighborhood movie house'
    
    print(line)
    print(title1)
    print(title2)
    print(date)
    print(line)
    print('Tickets            $ ' + format(subtotal))
    print('Sales Tax         $ ' + format(sales_tax))
    print('Total                $ ' + format(total))
    print(line)

############    call on main program to execute ###########
main()
