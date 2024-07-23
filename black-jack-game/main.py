from art import logo_blackjack
from os import system
import random

clear = lambda: system('cls')

STANDARD_DECK = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_track = {}


def deal_card():
    """Returns a random card from the deck."""
    return random.choice(STANDARD_DECK)


def calculate_score(deck_of_cards):
    """Calculates the sum of cards in deck, applying Ace card rule if possible."""
    if sum(deck_of_cards) == 21 and len(deck_of_cards) == 2:
        return 0
    if sum(deck_of_cards) > 21 and 11 in deck_of_cards:
        deck_of_cards[deck_of_cards.index(11)] = 1

    return sum(deck_of_cards)


def game_update(score1, score2):
    """Updates the game tracker dictionary."""
    game_track['Player'] = score1
    game_track['Dealer'] = score2


def compare(score1, score2):
    """Compares the total scores of Player and Dealer, following the Bust, Blackjack, and Draw rules."""
    if score1 == score2:
        return "It's a draw."
    elif score2 == 0:
        return "Dealer wins with a Blackjack."
    elif score1 == 0:
        return "You win with a Blackjack."
    elif score1 > 21:
        return "It's a bust. You lose!"
    elif score2 > 21:
        return "Dealer busts. You win!"
    else:
        winning_score = max(score1, score2)
        players_list = list(game_track.keys())
        scores_list = list(game_track.values())
        temp_position = scores_list.index(winning_score)
        return f"{players_list[temp_position]} wins!"


def main():
    user_cards = []
    for _ in range(2):
        user_cards.append(deal_card())

    dealer_cards = []
    for _ in range(2):
        dealer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)

    game_update(user_score, dealer_score)

    print(f"\tYour cards: {user_cards}, current score: {game_track['Player']}")
    print(f"\tDealer's first card: {dealer_cards[0]}")

    while 1:
        if calculate_score(user_cards) > 21:
            break

        usr_choice = input("Type 'y' to draw another card, type 'n' to stand: ")

        if usr_choice == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            game_update(user_score, dealer_score)
            print(f"\tYour cards: {user_cards}, current score: {game_track['Player']}")
            print(f"\tDealer's first card: {dealer_cards[0]}")
        elif usr_choice == 'n':
            break

    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
        game_update(user_score, dealer_score)

    print(f"\tDealer's final hand: {dealer_cards}, Dealer's final score: {game_track['Dealer']}")
    print(compare(user_score, dealer_score))


if __name__ == "__main__":
    while input("Do you want to play a game of Blackjack / 21? Type 'y' or 'n': ") != 'n':
        clear()
        print(logo_blackjack)
        main()

# TODO: Try to make the standard deck of cards limited (ie when a card is drawn, it cannot be picked again)
# TODO: Use list slicing and methods
# TODO: Move used cards at the end of list
# TODO: update slicer so that we only access available cards
