import random

secret_number = random.randint(10, 20)
guess = int(input("Guess the number: "))

match guess: 
    case 19:
        print("Congratulations, you guessed it!")
    case int() < 19:
        print("Nope, your guess is a bit low. Give it another shot!", guess)
    case int() > 19:
        print("Oops, your guess is a bit high. Try again!", guess)
    case _:
        print(secret_number)