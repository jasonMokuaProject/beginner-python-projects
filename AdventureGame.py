# Adventure Game
# This Script (Adventure game) was made to practice using if statements
Starter_Game = input("Do you want to start this adventure game? \n")

if Starter_Game == "yes":
    question_one = input("you are on a dirt road, you can go either right or left ").lower()
    if question_one == "right":
        print("\nYou have chosen to go right and have found a object on the floor.")
        question_two = input("Do you want to pick the object up and inspect it? ").lower()
        if question_two == "yes":
            print("\nThe object you picked up is worth 10 US dollars.")
            question_three = input("Do you want to trade this object and receive money? ").lower()
            if question_three == "yes":
                print("\nThis object is added to an ecommerce website")
    if question_one == "left":
        print("\nYou have chosen to turn left and see an old man struggling to to get out of his car ")
        question_two = input("should you help the man or continue walking? ").lower()
        if question_two == "yes":
            print("\nThe old man is grateful for your help and is offering you a gift")
            question_three = input("Do you want to accept or decline the gift? ").lower()
            if question_three == "accept":
                print("\nthe old man handed you an item worth 33 US dollars")
                question_four = input("\nDo you want to trade this object and receive money? ")
                if question_four == "yes":
                    print("This object is added to an ecommerce website")




