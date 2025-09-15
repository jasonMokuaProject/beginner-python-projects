import random

beginning_question = input("Do you want to play a guessing game?")

def random_number_game():
    random_number = random.randint(0,15)
    correct = True
    while correct:
        user_input = input("Guess a number between 0 and 15")
        if int(user_input) == random_number:
            correct = False
    print("Thank you for playing the guessing game! ")


if beginning_question.lower() == "yes":
    print("Let's begin")
    random_number_game()
else:
    print("Thank you for you time")

