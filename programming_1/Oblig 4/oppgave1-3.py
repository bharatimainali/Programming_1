#imported blackjack_module as bjm fra andre file.
import blackjack_module as bjm
#setting the starting money of chips 5.
chips = 5

#creating a wile loop for running the game.
game_playing = True
while game_playing == True:
    #generating a new set of cards and emptieng the hand of players and dealers.
    shuffled_deck = bjm.get_new_shuffled_deck()
    player_hand = []
    dealer_hand = []

    # checks if the player has 0 chips left. if so and the game is end.
    if chips <= 0:
        print("You have lost all the chips and lost the game. Thanks for playing")
        game_playing = False
        break
    print(f"You have {chips} chips.")
    # checks if the bet is valid, if not, print error
    try:
        bet = int(input("How many chips do you want to bet? "))
        if bet > chips:
            print("You cannot bet more chips than you have")
            continue
    except ValueError:
        print("That is not a number")
        continue
    except:
        print("An error occured. Try again.")
        continue

    # give the first two cards to player and dealer, and print them
    bjm.deal_initial_cards(player_hand, dealer_hand, shuffled_deck)
    bjm.print_initial_cards(dealer_hand, player_hand)

    # loop to check if round is still active
    round_playing = True
    while round_playing == True:
        player_value = bjm.calculate_hand_value(player_hand)
        # check if the player hit blackjack
        if player_value == 21:
            print(f"\nYou have a value of 21 and hit blackjack!")
            chips = chips + bet * 2
        else:
            # ask if player wants more cards or not
            choice = input("Do you wish to hit or stand? 1 for hit, 2 for stand: ")
            if choice == "1": # HIT
                print("You chose to hit")
                bjm.player_hit(player_hand, shuffled_deck)
                if bjm.calculate_hand_value(player_hand) > 21:
                    print("You have busted, over 21")
                    chips = chips - bet
                    break

            elif choice == "2": # STAND
                print("\nYou chose to stand")
                print("\nThe dealer has the following cards:")
                bjm.print_hand(dealer_hand)

                print("\nYou has the following cards:")
                bjm.print_hand(player_hand)

                # dealer gets new cards until value is >=17
                bjm.dealer_hit(dealer_hand, shuffled_deck)

                chips = bjm.print_result(player_hand, dealer_hand, chips, bet)
                round_playing = False

            else:
                print("That was not a valid option.")
    # ask the player if they want to keep playing after round is finished
    keep_playing = input("Do you want to play another round? y/n: ")
    if keep_playing == "y":
        print("Starting another round...")
    elif keep_playing == "n":
        print("The game has ended. Thank you for playing.")
        break
    else:
        print("That is not a valid option. y/n")