import random

secret_number = random.randint(10, 20)
#secret number is fifteen
guess = int(input("Guess a number between 10 and 20: "))

match guess: 
    case 15: 
        print("Congratulations, you guessed it")
    case int():
        if guess>15:
            print("Oops, your guess is a bit high. Try again!")
    case int():
        if guess<15:
            print("Nope, your guess is a bit low. Give it another shot!")
    case _:
        print(("Goodbye"))