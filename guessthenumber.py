# Libraries #
import random
import math

# Functions #
def computer_number(x,y):
    x = int(x)
    y = int(y)
    return random.randint(x,y)

def user_guess_number():
    return input("Give me your number: ")

def update_distance(user_number, number_guess):
    user_number = int(user_number)
    number_guess = int(number_guess)
    
    if abs(number_guess - user_number) <= 3:
        return print("Oh you are very close!")
    elif abs(number_guess-user_number) > 3 and abs(number_guess-user_number) <= 7:
        return print("Hmm... Quite close, make another guess.")
    else:
        return print("Your guess is quite off.")

# Main #
def main():
    attempts = 0 # Hold total number of attempts of the user.

    print("--- Welcome to the Number Guessing game, pick the range of the numbers you will be guessing! ---")
    x = input("It will start from: ")
    y = input("And will end on: ")

    number_guess = computer_number(x,y) # The number to guess.
    
    while True:
        print("Now make your guess!")
        user_number = user_guess_number() # User's guess.
        attempts +=1
        
        if int(user_number) == number_guess:
            print(f"Congrats, you have found the number! In {attempts} attempts.")
            break
        else:
            print("--- Status ---")
            update_distance(user_number, number_guess)

# Execute the program #
if __name__ == "__main__":
    main()
