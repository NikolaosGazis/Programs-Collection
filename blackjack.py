# Libraries #
import random

# Functions #
def menu():
    print("--- Game of 21 - Blackjack ---")
    print("1. Play")
    print("2. Rules")
    print("0. Exit\n")
    
def rules():
    print("1. The objective is to have a score closer to 21 as possible while the dealer and you, if you reach or go further than that, you go bust .") 
    print("2. Number cards are counted at their face value, Face cards are valued at 10 points each and Ace cards are valued at 1 or 11 points depending upon the total points in the hand.") 
    print("3. Each player starts with two cards, one of the dealer's cards is face down.") 
    print("4. Player can either 'hit' this means the player will receive another card, or the player can 'stand' meaning he does not want any other card but the ones he has got now.")
    print("5. Sometimes the dealer is allowed to hit until he has total cards that are above 17, dealers must stand if they have cards that are above 17") 
    print("6. If both the dealer and player have the same total, the game is tied and players bet is given back.")
    print("7. If a player is dealt an Ace and a cards worth ten points on the first two cards the player has a “Blackjack” which normally comes with 3 to 2 odds.") # To Do.
    print("8. The deck is shuffled again when the number of cards in it is not sufficient- remember the cards that have been played.\n") 

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

def bet(player_money):
    while True:
        try:
            initial_bet = int(input("[GAME] Place your opening bet -> "))
            if initial_bet > player_money:
                print(f"[GAME] Your bet exceeds your balance, you currently have {player_money}€!")
            else:
                return initial_bet
        except ValueError:
            print("[GAME] Your input has to be a valid number, try again.")

def player(player_hand, deck):
    while True:
        hand_value = hand_value_calculation(player_hand)
        print(f"[GAME] Your hand's value is: {hand_value}")
        if hand_value > 21:
            print("[GAME] You have busted! Better luck next time.")
            return False
        action = input("[GAME] Do you want to 'hit' or 'stand'? -> ")
        if action == 'hit':
            player_hand.append(deck.pop())
            print(f"[GAME] You drew: {player_hand[-1]}")
        elif action == 'stand':
            return True
        else:
            print("[GAME] Input is invalid, type either 'hit' or 'stand'!")

def dealer(dealer_hand, deck):
    print(f"[GAME] Dealer reveals his second card... {dealer_hand}")
    while hand_value_calculation(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print(f"[GAME] Dealer drew: {dealer_hand[-1]}")
    return hand_value_calculation(dealer_hand)

def compare(player_hand, dealer_hand, initial_bet, player_money):
    player_value = hand_value_calculation(player_hand)
    dealer_value = hand_value_calculation(dealer_hand)

    if dealer_value > 21:
        print("[GAME] Dealer has busted! You win!")
        return player_money + (2 * initial_bet)
    elif dealer_value > player_value:
        print("[GAME] Dealer wins! Better luck next time.")
    elif dealer_value < player_value:
        print("[GAME] You win!")
        return player_money + initial_bet

    return player_money

def game(player_money, deck):
    while player_money > 0:
        if len(deck) < 20: # If deck has less than 20 cards.
            print("[GAME] Deck needs resetting...\n")
            deck = deck_creation

        initial_bet = bet(player_money)
        player_money -= initial_bet

        # Initial Cards #
        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        # Table - Dealer shows only shows one card #
        print(f"[GAME] Your cards: {player_hand[0]}, {player_hand[1]}")
        print(f"[GAME] Dealer's cards: {dealer_hand[0]}\n")

        # Simulate Round #
        if player(player_hand, deck):
            dealer_value = dealer(dealer_hand, deck)
            player_money = compare(player_hand, dealer_hand, initial_bet, player_money)

        print(f"[GAME] Your current balance is {player_money}€.")

        replay = input("[GAME] Do you want to play again? (yes/no) -> ").lower()
        if replay != 'yes':
            break
            
    print("[GAME] Thank you for playing! Exiting...")

# Main #
def main():
    # Variables #
    player_money = 300
    deck = deck_creation()
    
    # Game Loop #
    while True:
        menu()
        choice = input("[GAME] What do you want to do? -> ")
        
        if choice == '1': # Play.
            game(player_money, deck)
        elif choice == '2': # Rules.
            rules()
        elif choice == '0':
            print("[GAME] Thank you for playing! Exiting...")
            break
        else:
            print("[Game] Your input is invalid, try again.")

if __name__ == "__main__":
    main()
