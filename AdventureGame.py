# Adventure Game
Starter_Game = input("Do you want to start this adventure game? ")

if Starter_Game == "yes":
    question_one = input("you are on a dirt road, you can go either right or left")
    if question_one == "right":
        print("You have chosen to go right and have found a object on the floor.")
        question_two = input("Do you want to pick the object up and inspect it? ")
        if question_two == "yes":
            print("The object you picked up is worth 10 US dollars.")
    if question_one == "left":
        print("You have chosen to turn left and see an old man struggling to to get out of his car ")
        question_two = input("should you help the man or continue walking? ")