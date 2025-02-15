# Author: Lucia Floan
# Date: Feb 14, 2025
# Title: Bank Balance 

# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

# Pseudocode:
# 1. Start the program
# 2. Ask the user to enter their monthly budget amount
# 3. Have a variable to keep track of the expenses (starts at 0)
# 4. Use a while loop to repeatedly ask the user for each expense until and exit 0 is entered
# 5. For each expense, add it to the total
# 6. Once the loop finishes, calculate the difference between the budget and the total spent
# 7. If the difference is positive, display how much the user is under budget
# 8. If the difference is negative, display how much the user is over budget
# 9. If the difference is zero, display that the user is exactly on their budget
# 10. End the program

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
    budget = float(input('Enter your budget for the month: '))

    while spent != 0:
        spent = float(input('Enter an expense (or 0 to exit): '))

        if spent != 0:
            total = total + spent

    difference = budget - total

    if difference > 0:
        print('You are under budget by $', difference)
    elif difference < 0:
        print('You are over budget by $', abs(difference))
    else:
        print('You are exactly on your budget.')

    ######################


if __name__ == '__main__':
    main()
