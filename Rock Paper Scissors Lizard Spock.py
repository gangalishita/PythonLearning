import random

# Possible actions
actions = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
# Shows what each action can beat
defeats = {
    "Rock": ["Scissors", "Lizard"],
    "Lizard": ["Paper", "Spock"],
    "Spock": ["Scissors", "Rock"],
    "Scissors": ["Lizard", "Paper"],
    "Paper": ["Spock", "Rock"]
}


# Generates a random action for the computer
def generate_computer_action():
    random_number = random.randint(0, 4)
    random_action = actions[random_number]
    return random_action


# Shows the user the actions they can play
print(""" These are the actions you can make>
Rock: 0
Paper: 1
Scissors: 2
Lizard: 3
Spock: 4 """)
print(" ")
# Asks user to choose the action they want to play
user_action = int(input("What is your action (number): "))
print(" ")

# Checks if the input is valid
if user_action not in [0, 1, 2, 3, 4]:
    user_action = int(input("Invalid Input. Please enter a valid action (0-4): "))
    print(" ")

# Generates the user's action for the number they selected
final_user_action = actions[user_action]
# Generates the computer's action using the random number
computer_action = generate_computer_action()

# Displays both the user and computer's actions
print("You chose: " + final_user_action)
print("Computer chose: " + computer_action)

# Shows the outcome of the game
if computer_action in defeats[final_user_action]:
    print("You win!")
elif computer_action == final_user_action:
    print("It's a tie!")
else:
    print("Computer wins!")

