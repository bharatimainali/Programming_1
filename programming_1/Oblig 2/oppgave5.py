# i importet the random and randrange.
from random import randrange

amount_of_darts = 3
total_scores = []
amount_of_players = int(input("How many players want to play? "))

# Using the for loop here.
for player in range(amount_of_players):
    print(f"Player {player + 1} is throwing now.")
    darts_thrown = 0
    total_player_score = 0
    # using the while loop
    while darts_thrown < amount_of_darts:

        # generating the random score between 0 to 60

        random_score = randrange(0, 60)
        total_player_score = total_player_score + random_score
        print(f"Player {player + 1} threw the dart and got {random_score} points.")
        darts_thrown = darts_thrown + 1
    print(f"Player {player + 1} got a total score of {total_player_score}.")
    total_scores.append(total_player_score)

# from random import randrange
#
# amount_of_darts = 3
# total_score = 0
#
# while amount_of_darts > 0:
#    print(f"You threw a dart.")
#    amount_of_darts = amount_of_darts - 1
#    random_score = randrange(0, 60)
#    total_score = total_score + random_score
#
# print(f"Your total score was {total_score}.")
