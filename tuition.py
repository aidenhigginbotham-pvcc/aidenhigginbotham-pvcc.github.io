# Name: Aiden Higginbotham, Albert Chen
# Prog Purpose: This program computes PVCC college tuition & fees based on number of credits
#    PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime
# define tuition & fee rates
RATE_TUITION_IN = 159.61
RATE_TUITION_OUT = 336.21
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# define global variables
inout = 1   # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarship_amt = 0

tuition_amt= 0
institution_fee = 0
capital_fee = 0
activity_fee = 0
total = 0
balance = 0

############    define program functions ###########
def main():
    
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        
        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno == "n" or yesno == "N":
            another_student = False
            print("Thank you for enrolling at PVCC. Enjoy the semester!")

def get_user_data():
       global inout, numcredits, scholarship_amt
       print('**** PIEDMONT VIRGINIA COMM COLLEGE Tuition & Fees ****!')
       inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
       numcredits = int(input("Number of credits registered for: "))
       scholarship_amt = float(input("Scholarship amount received: "))

def perform_calculations():
    global tuition_amt, institution_fee, capital_fee, activity_fee, total, scholarship_amt, balance
    
    if inout == 1:
        tuition_amt = numcredits * RATE_TUITION_IN
        capital_fee = 0
    else:
        tuition_amt = numcredits * RATE_TUITION_OUT
        capital_fee = numcredits * RATE_CAPITAL_FEE
        
    institution_fee = numcredits * RATE_INSTITUTION_FEE
    activity_fee = numcredits * RATE_ACTIVITY_FEE
    total = tuition_amt + institution_fee + activity_fee + capital_fee
    balance = total - scholarship_amt
  
def display_results():
    line = '----------------------------------------------'
    currency = '8,.2f'
    dt_full = str(datetime.datetime.now())
    dt_short = dt_full[0:16]
    title1 = '**** PIEDMONT VIRGINIA COMM COLLEGE****'

    print(line)
    print(title1)
    print('        Date/Time:     ' , dt_short)
    print(line)
    print('Tuition     $' + format(tuition_amt, currency))
    print('Capital Fee     $' + format(capital_fee, currency))
    print('Institution Fee    $' + format(institution_fee, currency))
    print('Activity fee     $' + format(activity_fee, currency))
    print('Total     $' + format(total, currency))
    print('Scholarship    $' + format(scholarship_amt, currency))
    print(line)
    print('Balance     $' + format(balance, currency))
    print(line)
    
############    call on main program to execute ###########
main()
