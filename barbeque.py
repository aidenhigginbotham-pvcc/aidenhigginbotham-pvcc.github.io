# Name: Aiden Higginbotham
# Prog Purpose: This program finds the cost of a meal at Branch Barbeque Buffet
#   Price for an adult meal: $19.95
#   Price for a child meal: $11.95
#   Service fee: 10%
#   Sales tax rate: 6.2%

import datetime

############    define global variables ###########
# define tax rate, service fee, and prices
ADULT_MEAL = 19.95
CHILD_MEAL = 11.95
SERVICE_FEE = .010
SALES_TAX_RATE = .062

# define global variables
num_adult_meals = 0
num_child_meals = 0
service_fee = 0
sales_tax = 0
total = 0

############    define program functions ###########
def main():
    prompt_in = "\nWould you like to order again (Y or N) "
    goodbye_msg = "Thank you for your order. Enjoy your meal!"
    more_meals = True
    
    while more_meals:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input(prompt_in)
        if (yesno.upper() == "N"):
            more_data = False
            print(goodbye_msg)
            
def get_user_data():
    global num_adult_meals, num_child_meals
    num_adult_meals = int(input("Number of adult meals: "))
    num_child_meals = int(input("Number of child meals:"))
def perform_calculations():
    global num_adult_meals, num_child_meals, subtotal, service_fee, sales_tax, total
    num_adult_meals = num_adult_meals * ADULT_MEAL
    num_child_meals = num_child_meals * CHILD_MEAL
    subtotal = num_adult_meals + num_child_meals
    service_fee = subtotal * SERVICE_FEE
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax + service_fee

def display_results():
    line = '----------------------------------------------'
    currency = '8,.2f'
    date = str(datetime.datetime.now())
    title1 = '**** Branch Barbeque Buffet ****'
    
    print(line)
    print(title1)
    print(date)
    print(line)
    print('Adult meals           $ ' + format(num_adult_meals, '8,.2f'))
    print('Child meals           $ ' + format(num_child_meals, '8,.2f'))
    print('Total meals           $ ' + format(subtotal, '8,.2f'))
    print('Service Fee     $ ' + format(service_fee, '8,.2f'))
    print('Sales Tax         $ ' + format(sales_tax, '8,.2f'))
    print('Total                $ ' + format(total, '8,.2f'))
    print(line)

############    call on main program to execute ###########
main()
