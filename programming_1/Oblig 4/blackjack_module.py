import random

full_deck = {"Two of clubs": 2, "Three of clubs": 3, "Four of clubs": 4, "Five of clubs": 5, "Six of clubs": 6,
             "Seven of clubs": 7, "Eight of clubs": 8, "Nine of clubs": 9, "Ten of clubs": 10,
             "Jack of clubs": 10, "Queen of clubs": 10, "King of clubs": 10, "Ace of clubs": 11,
             "Two of diamonds": 2, "Three of diamonds": 3, "Four of diamonds": 4, "Five of diamonds": 5,
             "Six of diamonds": 6, "Seven of diamonds": 7, "Eight of diamonds": 8, "Nine of diamonds": 9,
             "Ten of diamonds": 10, "Jack of diamonds": 10, "Queen of diamonds": 10, "King of diamonds": 10,
             "Ace of diamonds": 11,
             "Two of hearts": 2, "Three of hearts": 3, "Four of hearts": 4, "Five of hearts": 5, "Six of hearts": 6,
             "Seven of hearts": 7, "Eight of hearts": 8, "Nine of hearts": 9, "Ten of hearts": 10,
             "Jack of hearts": 10, "Queen of hearts": 10, "King of hearts": 10, "Ace of hearts": 11,
             "Two of spades": 2, "Three of spades": 3, "Four of spades": 4, "Five of spades": 5, "Six of spades": 6,
             "Seven of spades": 7, "Eight of spades": 8, "Nine of spades": 9, "Ten of spades": 10,
             "Jack of spades": 10, "Queen of spades": 10, "King of spades": 10, "Ace of spades": 11,
             }


def get_new_shuffled_deck():
    deck = list(full_deck.keys())
    random.shuffle(deck)
    return deck


def get_card_value(card):
    return full_deck[card]


def calculate_hand_value(hand):
    hand_value = 0
    for card in hand:
        if get_card_value(card) == 11:
            hand_value += 1
        else:
            hand_value += get_card_value(card)

    return hand_value

def deal_initial_cards(player_hand, dealer_hand, shuffled_deck):
    card1 = shuffled_deck.pop()
    card2 = shuffled_deck.pop()
    card3 = shuffled_deck.pop()
    card4 = shuffled_deck.pop()
    dealer_hand.extend([card1, card2])
    player_hand.extend([card3, card4])

def print_initial_cards(dealer_hand, player_hand):
    print(f"The cards have been dealt. You have a {player_hand[0]} and a {player_hand[1]}, with a total value of {calculate_hand_value(player_hand)}.The dealers visible card is a {dealer_hand[0]}, with a value of {get_card_value(dealer_hand[0])}" )

def print_hand(hand):
    for card in hand:
        print(card)
    print(f"With a total value of {calculate_hand_value(hand)}")

def print_result(player_hand, dealer_hand, chips, bet):
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21:
        print("Player won, dealer got over 21")
        chips = chips + bet
        return chips
    elif player_value > dealer_value:
        print("Player won, player value is higher than dealer value")
        chips = chips + bet
        return chips
    elif dealer_value > player_value:
        print("You lost, the dealer won. The dealer had a higher value.")
        chips = chips - bet
        return chips
    else:
        print("It's a tie. You both have the same value.")
        return chips


def player_hit(player_hand, shuffled_deck):
    new_card = shuffled_deck.pop()
    player_hand.append(new_card)
    print(f"You received {new_card} and now have a total value of {calculate_hand_value(player_hand)}")

def dealer_hit(dealer_hand, shuffled_deck):
    while calculate_hand_value(dealer_hand) < 17:
        new_card = shuffled_deck.pop()
        dealer_hand.append(new_card)
        print(f"The dealer got a new card: {new_card} with a value of {get_card_value(new_card)}.")