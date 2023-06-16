#Capstone Project 1
#A program with 2 finance calculators for a user.
#An investment calculator and a Home loan repayment calculator.

import sys
import math

#Formulas in this program.
#Simple interest: A = P(1 + r * t)
#Compound interest: A = P(1 + r) ^ t
#Monthly Home Loan re-payment: x = (i.P)/(1 - ((1+i)^(-n)))
#                              x = (i/12).(1/(1-(1+i/12)^(-n))).P

# Displaying info to user and requesting input
choose = input("""Choose either 'investment' or 'bond' from the menu below to proceed:

Investment     - to calculate the amount of interest you'll earn on interest.
Bond           - to calculate the amount you'll have to pay on a home loan.\n""")
print("")
choose = choose.lower() # Casting user input to lower case to avoid errors.

# comparing to see if input is valid. Executing appropriate instructions.
if (choose != "investment") & (choose != "bond"):
    choose = input("""Your entry does not match with the selection. Please enter
                   'investment' or 'bond' below:\n""")
else:
    print("Thank you for your selection.")
    choose = choose.lower()
    print("")

# comparing statement to conditions set and executing appropriate instructions.
if choose == "bond":
    print("""Please provide the following information to calculate your monthly home 
loan repayment ammount:""")
    value = int(input("Present value of the house: R"))   # requesting input from user.
    rate = int(input("The yearly interest rate on the home loan: "))
    month = int(input("Over how many months do you wish to pay off your loan? "))
    rate = (int(rate) / 100)       # dividing by 100 to get percentage.
    rate = round(rate, 2)
    re_pay =(rate / 12) * (1 / (1 - (1 + rate / 12)**(-month)))*value # Provided comments at end of code.
    #re_pay = (rate * value) / (1 - ((1 + rate)**(-month))) 
    re_pay = round(re_pay, 2)         # rounding answer
# displaying info to user.
    print("")
    print("Your monthly re-payment ammount will be R" + str(re_pay) + ".")
    print("")
# comparing statement against conditions set.
elif choose == "investment":
    # display info to user and requesting input.
    print("Please provide the following information for calculation purposes:")
    deposit = int(input("The ammount you are depositing: R"))
    rate = int(input("The interest rate received on investment: "))
    num_years = int(input("The number of years you plan to invest your money: "))
    interest = input("""Would you like 'simple interest' or 'compound
interest' on your investment? """)
    print("")
    rate = rate / 100 # dividing by 100 to get percentage
    simple_payout = deposit * (1 + rate * num_years)
    compound_payout = deposit* math.pow((1 + rate),num_years)
    compound_interest = compound_payout - deposit
    compound_interest = round(compound_interest, 2)
    simple_interest = simple_payout - deposit
    simple_interest = round(simple_interest, 2)

    if interest == "simple":
        print("""Ammount of interest earned over """ + str(num_years) + """ years is R"""
              + str(simple_interest) + """.""") # displaying info to user based on selection.
    else:
        interest == "compound"
        print("""Ammount of interest earned over """ + str(num_years) + """ years is R"""
              + str(compound_interest) + """.""")  # displaying info to user based on selection.
        print("")

#waits for users input before closing program.    
input("Press 'enter' key to quit.")
sys.exit

# formula given for monthly home loan re-payment gives a very high monthly
# re-payment. Found different formula on this website:
# https://www.statology.org/python-monthly-payment-function/
# can test both formulas above to see the difference in ammounts.
    
    
    
    
    


 
