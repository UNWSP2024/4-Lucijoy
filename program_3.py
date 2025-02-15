# Author: Lucia Floan
# Date: Feb 14, 2025
# Title: Average Rainfall


# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    ######################
    number_years = int(input('Enter the number of years: '))
    
    total_rainfall = 0
    number_months = 0

        for year in range (1, number_years + 1):
            print(f'\nYear {year}:')

            for month in range(1, 13):
                rainfall = float(input(f'Enter the rainfall for month {month} (in inches): '))

                total_rainfall += rainfall
                number_months += 1

            average_rainfall = total_rainfall / number_months


            print(f'\nTotal number of months: {number_months}')
            print(f'Total inches of rainfall: {total_rainfall}')
            print(f'Average rainfall per month: {average_rainfall:.2f} inches')
            
    
    ######################    


if __name__ == '__main__':
    main()
