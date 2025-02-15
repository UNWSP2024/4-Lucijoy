# Author: Lucia Floan
# Date: Feb 14, 2025
# Title: Movie Tix

# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
    current_tickets = 0
    amount_movies = int(input('How many movies are you buying tickets for? '))
    for i in range(amount_movies):
        movie_name = input('Enter movie name: ')
        tickets = int(input('How many tickets for ' + movie_name + '? '))
        current_tickets = current_tickets + tickets

    print('Total amount of purchased tickets:', current_tickets)
    ######################


if __name__ == '__main__':
    main()
