#create a definition
import random

def guess_the_number(number):
    #The computer randomly selects a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the guess number!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    #Ask the player for a guess 
    while True:
        try: 
            guess = int(input("Enter your guess:    "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Enter a number between 1 and 100")
            elif guess < number_to_guess:
                print("Too low! Try again")
            elif guess > number_to_guess:
                print("Too high! Try again")
            else:
                print("Congratulations! You've entered the number in {attempts} attempts")
                break
        except ValueError:
            print("Invalid input. Please enter a valid input")

if __name__ == "__main__":
    guess_the_number()