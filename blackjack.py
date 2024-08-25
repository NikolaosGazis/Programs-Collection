# Libraries #
import random

# Functions #
def menu():
    print("--- Game of 21 - Blackjack ---")
    print("1. Play")
    print("2. Rules")
    print("0. Exit\n")
    
def rules():
    pass
    
def deck_creation():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = cards * 4 # Each deck has 4 copies of each card.
    random.shuffle(deck)
    return deck

def card_value(card):
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 11
    else:
        return int(card)

def hand_value_calculation(hand):
    value = sum(card_value(card) for card in hand)
    aces = hand.count('A')
    
    while value > 21 and aces > 0: # Treat Ace's value as 1 so the player doesn't bust.
        value -= 10
        aces -= 1
        
    return value

# Main #
def main():
    # Variables #
    player_money = 300
    deck = deck_creation()
    
    # Game Loop #
    while True:
        menu()
        choice = input("[GAME] What do you want to do?")
        
        if choice == '1': # Play.
            if len(deck) < 15: # Deck needs reset.
                print("[GAME] Deck needs resetting...\n")
                deck = deck_creation
        
            # Bet and Balance #
            initial_bet = int(input("[GAME] Place your opening bet:"))
            if initial_bet > player_money:
                print(f"[GAME] Your bet exceeds your balance, you currently have {player_money}€!")
                continue
            else:
                player_money -= initial_bet
                print(f"[GAME] You placed {initial_bet} and your remaining balance is {player_money}€.")
            
            # Initial Cards #
            player_hand = [deck.pop(), deck.pop()]
            dealer_hand = [deck.pop(), deck.pop()]
            
            # Table - Dealer shows only shows one card #
            print(f"[GAME] Your cards: {player_hand[0]}, {player_hand[1]}")
            print(f"[GAME] Dealer cards: {dealer_hand[0]}\n")
            
            # Player Turn #
            while True:
                hand_value = hand_value_calculation(player_hand)
                print(f"[GAME] Your hand value is: {hand_value}")
                if hand_value > 21:
                    print(f"[GAME] You busted!")
                action = input("[GAME] Do you wish to 'hit' or 'stand'?").lower()
                if action == 'hit':
                    pass
                elif action == 'stand':
                    break
                else:
                    print("[GAME] Input is invalid, type 'hit' or 'stand'.")
            
            # Dealer Turn #
            
            # Ask the player if he wishes to play again #
            replay = input("[GAME] Do you want to play again? (yes/no)").lower()
            if replay != 'yes':
                break
        elif choice == '2': # Rules.
            pass
        elif choice == '0':
            print("[GAME] Thank you for playing! Exiting...")
        else:
            print("[Game] Your input is invalid, try again.")

if __name__ == "__main__":
    main()
