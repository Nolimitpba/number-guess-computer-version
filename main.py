import random

def guess(x):
    guess = 0
    random_number = random.randint(1, x)
    while guess != random_number:
        guess = int(input("guess the random number: "))
        if guess < random_number:
            print("Too low, try again")
        elif guess > random_number:
            print("Too high try again")

    print(f"Yay you have guessed the number {guess} correctly!!!")

guess(10)    