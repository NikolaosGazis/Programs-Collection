# Libraries #
import random

# Definements #
teams = { # Teams from the League with their strength value.
    'Olympiacos': 10,
    'Panathinaikos': 9,
    'AEK': 8,
    'PAOK': 8,
    'Aris': 7,
    'Asteras Tripolis': 6,
    'OFI': 6,
    'Atromitos': 6,
    'Panserraikos': 5,
    'Lamia': 4,
    'Panaitolikos': 4,
    'Levadeiakos': 3,
    'Kallithea': 3,
    'Volos': 2
}

# Functions #
def menu():
    print("0. Exit")
    print("1. Make a bet slip")
    print("2. Check your Balance")
    print("3. Check this gameweek's matches")

def display_gameweek():
    pass

def display_slip():
    pass

def calculate_odds():
    pass

def simulate():
    pass

# Main #
def main():
    money = 5
    gameweek = 0
    print("--- Greek Superleague Online Betting ---\n")
    print(f"[SYSTEM] You currently have: {money}\n")

    while True:
        menu()
        gameweek += 1
        action = int(input("[SYSTEM] What do you want to do? -> "))
        if action == 0: # Exit.
            print("Thank you for playing. Exiting...")
            break
        elif action == 1: # Betting Slip.
            pass
        elif action == 2: # Check Balance.
            pass
        elif action == 3: # Gameweek's matches.
            pass


# Execute the program #
if __name__ == "__main__":
    main()
    