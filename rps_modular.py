games_total = 0
player1_invalid = 0
player2_invalid = 0
player1_wins = 0
player2_wins = 0
ties = 0
inputs = ["rock","paper","scissors"]

while games_total < 10:
    '''
    Lines 15-22 prompts Player 1 and Player 2 for their selection. The while loops will continue to loop indefinitely
    until the player selection is a valid input contained in the input list. For each invalid attempt, the number of
    invalid attempts is increased by 1.
    '''
    player1_selection = input("Player 1 plays ")
    while player1_selection not in inputs:
        player1_invalid += 1
        player1_selection = input("Player 1 plays ")
    player2_selection = input("and Player 2 plays ")
    while player2_selection not in inputs:
        player2_invalid += 1
        player2_selection = input("and Player 2 plays ")

    player1_index = inputs.index(player1_selection) #Index of valid Player 1 selection in input list
    player2_index = inputs.index(player2_selection) #Index of valid Player 2 selection in input list

    if (player1_index + 1)%3 == player2_index:  #Player 2 index 1 larger than Player 1. Player 2 is the winner
        player2_wins += 1
    elif player1_index == player2_index: #Player 1 and Player 2 index are equal
        ties += 1
    else:
        player1_wins +=1

    games_total += 1

print(f"Player 1 won {player1_wins} games, Player 2 won {player2_wins} games, and there were {ties} ties\
. Player 1 made {player1_invalid} invalid gestures and Player 2 made {player2_invalid} invalid gestures")