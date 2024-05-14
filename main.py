import sys, random, getpass  # sys for quit, random for computer pick, getpass for multiplayer

# Options Constant / 1 for Rock, 2 for Paper, 3 for Scissors
OPTIONS = ["1", "2", "3"]

# Scoring Variables 
player_one_wins = 0
player_two_wins = 0
computer_wins = 0

def determine_winner(choice1, choice2, OPTIONS):
    """
    Determines the winner between two choices.
    Updates global win counters accordingly.
    """
    global player_one_wins, player_two_wins, computer_wins
    
    if choice1 == choice2:
        print("It's a tie!!\n")

    # Finding the winning conditions Player 1
    if (choice1 == OPTIONS[0] and choice2 == OPTIONS[2]) or (choice1 == OPTIONS[1] and choice2 == OPTIONS[0]) or (choice1 == OPTIONS[2] and choice2 == OPTIONS[1]):
        player_one_wins += 1
        if menu_option == "1":
            print("You Win!\n")
        elif menu_option == "2":
            print("Player One Wins!\n")
    # Finding the winning conditions for Computer or Player 2
    elif (choice2 == OPTIONS[0] and choice1 == OPTIONS[2]) or (choice2 == OPTIONS[1] and choice1 == OPTIONS[0]) or (choice2 == OPTIONS[2] and choice1 == OPTIONS[1]):
        if menu_option == "1":
            computer_wins += 1
            print("Computer Wins.\n")
        elif menu_option == "2":
            player_two_wins += 1
            print("Player Two Wins!\n")

def final_score(score1, score2):
    """
    Prints the final score and determines the overall winner.
    """
    if score1 == score2:
        if menu_option == "1":
            print("\nYour Score:", player_one_wins)
            print("Computer Score:", computer_wins)
            print("\nIts a Tie")
        elif menu_option == "2":
            print("\nPlayer One Score:", player_one_wins)
            print("Player Two Score:", player_two_wins)
            print("\nIts a Tie")
    elif score1 > score2:
        if menu_option == "1":
            print("\nYour Score:", player_one_wins)
            print("Computer Score:", computer_wins)
            print("\nYou Win!")
        elif menu_option == "2":
            print("\nPlayer One Score:", player_one_wins)
            print("Player Two Score:", player_two_wins)
            print("\nPlayer One Wins!")
    else:
        if menu_option == "1":
            print("\nYour Score:", player_one_wins)
            print("Computer Score:", computer_wins)
            print("\nComputer Wins")
        elif menu_option == "2":
            print("\nPlayer One Score:", player_one_wins)
            print("Player Two Score:", player_two_wins)
            print("\nPlayer Two Wins!")

def player_vs_computer():
    """
    Handles the game logic for Player vs Computer mode.
    """
    while True:
        # Get User Input 
        user_option = input("Type '1' for Rock, '2' for Paper, '3' for Scissors or 'q' to quit: ")

        # Get Random Computer Option
        computer_option = random.choice(OPTIONS)

        # Print Player Option and Check quit
        if user_option == 'q':
            break
        elif user_option == '1':
            print("\nYou picked Rock")
        elif user_option == '2':
            print("\nYou picked Paper")
        elif user_option == '3':
            print("\nYou picked Scissors")

        # Print Computer Option 
        if computer_option == '1':
            print("Computer picked Rock")
        elif computer_option == '2':
            print("Computer picked Paper")
        elif computer_option == '3':
            print("Computer picked Scissors")
        
        determine_winner(user_option, computer_option, OPTIONS)
        
    final_score(player_one_wins, computer_wins)
    player_one_wins = 0
    computer_wins = 0

def player_vs_player():
    global player_one_wins, player_two_wins

    while True:
        # Get Player One Input
        player_one_option = getpass.getpass("Player One - Type '1' for Rock, '2' for Paper, '3' for Scissors or 'q' to quit: ")
        if player_one_option == 'q':
            break

        # Get Player Two Input
        player_two_option = getpass.getpass("Player Two - Type '1' for Rock, '2' for Paper, '3' for Scissors or 'q' to quit: ")
        if player_two_option == 'q':
            break

        # Print Player One Option
        if player_one_option == '1':
            print("\nPlayer One picked Rock")
        elif player_one_option == '2':
            print("\nPlayer One picked Paper")
        elif player_one_option == '3':
            print("\nPlayer One picked Scissors")

        # Print Player Two Option
        if player_two_option == '1':
            print("Player Two picked Rock")
        elif player_two_option == '2':
            print("Player Two picked Paper")
        elif player_two_option == '3':
            print("Player Two picked Scissors")

        determine_winner(player_one_option, player_two_option, OPTIONS)

    final_score(player_one_wins, player_two_wins)
    player_one_wins = 0
    player_two_wins = 0

# Game Loop
while True:
    # Main Menu
    print("\n-----------------------------")
    print("     Rock Paper Scissors     ")
    print("-----------------------------")
    print()
    print("    1. Player vs Computer    ")
    print("    2. Player vs Player      ")
    print("    3. Quit                  ")
    print()
    # Get user main menu input
    menu_option = input(">> ")

    # Play against Computer 
    if menu_option == "1":
        player_vs_computer()
    # Play against another Player
    elif menu_option == "2":
        player_vs_player()
    # Exit Game
    elif menu_option == "3":
        print("Thanks for Playing!")
        sys.exit()
    # Error Handling
    else:
        print("\nInvalid Input. Please select 1-3.")