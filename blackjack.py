# Libraries #
import random

# Functions #
def menu():
    print("--- Game of 21 - Blackjack ---\n")
    print("1. Play\n")
    print("2. Rules\n")
    print("0. Exit\n")
    
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

def hand_value(hand_cards):
    pass

# Main #
def main():
    # Variables #
    player_money = 300
    deck = deck_creation()
    
    # Game Loop #
    while True:
        if len(deck) < 15: # Deck needs reset.
            print("[GAME] Deck needs resetting...\n")
            deck = deck_creation
        
        # Bet and Balance #
        initial_bet = int(input("[GAME] Place your opening bet -> "))
        if initial_bet > player_money:
            print("[GAME] Your bet exceeds your balance, try again.")
            continue
        else:
            player_money -= initial_bet
            print(f"[GAME] You placed {initial_bet} and your remaining balance is {player_money}.")
        
        # Game #
        player_hand = []
        for _ in range(2):
            card = deck.pop()
            player_hand.append(card)
            print(f"[GAME] You drew the following card: {card}")
        
        # Calculate hand value #
        # Ask the player if he uses to draw another card - place more money - stand #
        # Announce the results #
        # Ask if the player wants to play again #
        # Dealer logic #

if __name__ == "__main__":
    main()
