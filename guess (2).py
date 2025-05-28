#destiney Cardenas
#11/12/2024

import random


def guess_game():
    print("Welcome to the GUESSING GAME")
    print("CHOOSE YOUR LEVEL")
    level = int(input("Choose level 1, 2, or 3 "))

    if level == 1:
        print("Guess the Number I'm thinking of 1 -> 10 ")
        print("You get three guesses.")
        secret = random.randint(1,10) #integer
        guess = int(input("Enter Guess 1: "))#integer
        if guess == secret:
            print("You guessed it!")
            print("Do you want to try again? ")
            again = input("yes or no ")
            if again == "yes":
                return guess_game()
            elif again == "no":
                print("Thanks for playing!")
            quit()
        elif guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low :(")
        guess = int(input("Enter Guess 2: "))
        if guess == secret:
            print("You guessed it!")
            print("Do you want to try again? ")
            again = input("yes or no ")
            if again == "yes":
                return guess_game()
            elif again == "no":
                print("Thanks for playing!")
            quit()
        elif guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low :(")
        guess = int(input("Enter Guess 3: "))
        if guess == secret:
            print("You guessed it!")
            print("Do you want to try again? ")
            again = input("yes or no ")
            if again == "yes":
                return guess_game()
            elif again == "no":
                print("Thanks for playing!")
            quit()
        elif guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low :(")
        if guess != secret:
            print("The number was " + str(secret))
        print("Do you want to try again? ")
        again = input("yes or no ")
        if again == "yes":
            return guess_game()
        elif again == "no":
            print("Thanks for playing!")

    elif level == 2:
        print("Guess the Number I'm thinking of -10 -> 15 ")
        print("You get three guesses.")
        secret = random.randint(1,10) #integer
        guess = int(input("Enter Guess 1: "))#integer
        if guess == secret:
            print("You guessed it!")
            print("Do you want to try again? ")
            again = input("yes or no ")
            if again == "yes":
                return guess_game()
            elif again == "no":
                print("Thanks for playing!")
            quit()
        elif guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low :(")
        guess = int(input("Enter Guess 2: "))
        if guess == secret:
            print("You guessed it!")
            print("Do you want to try again? ")
            again = input("yes or no ")
            if again == "yes":
                return guess_game()
            elif again == "no":
                print("Thanks for playing!")
            quit()
        elif guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low :(")
        guess = int(input("Enter Guess 3: "))
        if guess == secret:
            print("You guessed it!")
            print("Do you want to try again? ")
            again = input("yes or no ")
            if again == "yes":
                return guess_game()
            elif again == "no":
                print("Thanks for playing!")
            quit()
        elif guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low :(")
        if guess != secret:
            print("The number was " + str(secret))
        print("Do you want to try again? ")
        again = input("yes or no ")
        if again == "yes":
            return guess_game()
        elif again == "no":
            print("Thanks for playing!")

    elif level == 3:
        print("Guess the Number I'm thinking of -50 -> 50 ")
        print("You get three guesses.")
        secret = random.randint(1,10) #integer
        guess = int(input("Enter Guess 1: "))#integer
        if guess == secret:
            print("You guessed it!")
            print("Do you want to try again? ")
            again = input("yes or no ")
            if again == "yes":
                return guess_game()
            elif again == "no":
                print("Thanks for playing!")
            quit()
        elif guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low :(")
        guess = int(input("Enter Guess 2: "))
        if guess == secret:
            print("You guessed it!")
            print("Do you want to try again? ")
            again = input("yes or no ")
            if again == "yes":
                return guess_game()
            elif again == "no":
                print("Thanks for playing!")
            quit()
        elif guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low :(")
        guess = int(input("Enter Guess 3: "))
        if guess == secret:
            print("You guessed it!")
            print("Do you want to try again? ")
            again = input("yes or no ")
            if again == "yes":
                return guess_game()
            elif again == "no":
                print("Thanks for playing!")
            quit()
        elif guess > secret:
            print("Too high!")
        elif guess < secret:
            print("Too low :(")
        if guess != secret:
            print("The number was " + str(secret))
        print("Do you want to try again? ")
        again = input("yes or no ")
        if again == "yes":
            return guess_game()
        elif again == "no":
            print("Thanks for playing!")


#main
guess_game()
