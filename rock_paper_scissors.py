def get_choice(player):
    choice = input(f"{player}, enter your choice (rock, paper, scissors): ").strip().lower()
    if choice not in ["rock", "paper", "scissors"]:
        print("Invalid input")
        return None
    return choice

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "It's a tie!"
    elif (choice1 == "rock" and choice2 == "scissors") or \
         (choice1 == "scissors" and choice2 == "paper") or \
         (choice1 == "paper" and choice2 == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Основная логика игры
choice1 = get_choice("Player 1")
if choice1:
    choice2 = get_choice("Player 2")
    if choice2:
        result = determine_winner(choice1, choice2)
        print(result)