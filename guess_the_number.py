# Libraries #
import random

# Functions #
def random_number(start, end):
    return random.randint(start, end)

def user_guess_number():
    while True:
        try:
            return int(input("[SYSTEM] Enter your guess: "))
        except:
            print("Enter a valid integer.")

def distance(user_guess, target):
    difference = abs(target - user_guess)

    if difference == 0: # Found.
        return "Correct"
    elif difference <= 5:
        print("Pretty close!")
    elif difference <= 10:
        print("Quite close, make another guess.")
    else:
        print("Your guess is quite off.")

# Main #
def main():
    print("--- Welcome to the Number Guessing game! ---")
    
    # Get user input if he wants to have a custom range for the number #
    custom_range_val = input("[SYSTEM] You want to set up a custom range for the number? (y/n): ").strip().lower()

    if custom_range_val == 'y':
        # User defines the range #
        while True:
            try:
                start = int(input("Start of range: "))
                end = int(input("End of range: "))
                if start >= end:
                    print("Starting point exceeds the ending, try again.")
                else:
                    break
            except ValueError:
                print("[SYSTEM] Please enter a valid integer!")
    else:
        # Default #
        start = 0
        end = 100
        print(f"[SYSTEM] The number will be between {start} and {end}!")
    
    # Set the random number #
    target = random_number(start, end)
    attempts = 0
    
    while True:
        print("[SYSTEM] Now make your guess! -> ")
        user_number = user_guess_number()
        attempts +=1

        # Update user on guess #
        if distance(user_number, target) == "Correct":
            print(f"Congratulations, you have found number {target} in {attempts} attempts!")
            break

# Execute the program #
if __name__ == "__main__":
    main()
