# This is a basic game of rock, paper and scissors created with python
# RPS stands for Rock Paper Scissors

import random

play_or_not = True
choices = ["rock","paper","scissor"]


def RPS_Game():
    gameon = True
    player_score = 0
    computer_score = 0
    while gameon:


        if player_score == 3:
            print("Player Won")
            gameon = False
            break
        if computer_score == 3:
            print("Computer Won")
            gameon = False
            break

        playerChoice = input("Select rock, paper, scissor: ").lower()
        randomcomputerpick = random.randint(0,2)
        computerChoice = choices[randomcomputerpick]
        if playerChoice == "rock" and computerChoice == "rock":
            print("Draw as you both picked rock")
        elif playerChoice == "rock" and computerChoice == "paper":
            print("computer wins \n computer picked paper \n player picked rock")
            computer_score += 1
        elif playerChoice == "rock" and computerChoice == "scissor":
            print("player wins \n computer picked scissor \n player picked rock")
            player_score += 1
        elif playerChoice == "paper" and computerChoice == "paper":
            print("Draw as you both picked paper")
        elif playerChoice == "paper" and computerChoice == "rock":
            print("player wins \n computer picked rock \n player picked paper")
            player_score += 1
        elif playerChoice == "paper" and computerChoice == "scissor":
            print("computer wins \n computer picked scissor \n player picked paper")
            computer_score += 1
        elif playerChoice == "scissor" and computerChoice == "rock":
            print("computer wins \n computer picked rock \n player picked scissor")
            computer_score += 1
        elif playerChoice == "scissor" and computerChoice == "scissor":
            print("Draw as you both picked paper")
        elif playerChoice == "scissor" and computerChoice == "paper":
            print("player wins \n computer picked paper \n player picked scissor")
            player_score += 1



yesorno = input("Do you want to play a game of rock, paper and scissors? ")
if yesorno == "yes":
    RPS_Game()
