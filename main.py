from art import logo
import random

def add_card(cards_list, cards):
    cards_list.append(random.choice(cards))

def update_card(cards_list):
    checked_cards_list = []
    for i in range(len(cards_list)):
        if sum(cards_list) > 21 and cards_list[i] == 11:
            checked_cards_list.append(1)
        else:
            checked_cards_list.append(cards_list[i])
    return checked_cards_list

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

game_over = False

while not game_over:
    user_cards = []
    dealer_card = []

    choice = input("Do you want to play a game of Blackjack? Type 'Y' or 'N':").lower()

    if choice == 'y':
        print(logo)

        for i in range(2):
            add_card(user_cards, cards)
            add_card(dealer_card, cards)

        user_score = sum(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {dealer_card[0]}")

        end_game = False

        while not end_game:
            more_card = input("Type 'Y' to get another card, type 'N' to pass : ").lower()
            if more_card == 'y':
                add_card(user_cards, cards)
                if sum(user_cards) > 21:
                    user_cards = update_card(user_cards)
                    if sum(user_cards) > 21:
                        print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
                        print(f"Computer's final hand: {dealer_card}, final score: {sum(dealer_card)}")
                        print(f"Your went over. You lose.")
                        end_game = True
                    else:
                        print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                        print(f"Computer's first card: {dealer_card[0]}")
                else:
                    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
                    print(f"Computer's first card: {dealer_card[0]}")


            elif more_card == 'n':
                while sum(dealer_card) < 17:
                    add_card(dealer_card, cards)
                dealer_card = update_card(dealer_card)
                dealer_score = sum(dealer_card)
                user_score = sum(user_cards) 
                print(f"Your final hand: {user_cards}, final score: {user_score}")
                print(f"Computer's final hand: {dealer_card}, final score: {dealer_score}")
                if dealer_score > 21:
                    print("Dealer went over. You win.")
                elif dealer_score > user_score:
                    print("You lose.")
                elif user_score > dealer_score:
                    print("You win.")
                else:
                    print("Draw.")
                end_game = True

    elif choice == 'n':
        print("Bye Bye!")
        game_over = True
