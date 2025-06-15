import random

randNum = random.randint(1, 100)
wrongGuesses = 0

while True:
    print("guess the number! (1-100)")
    guess = int(input("your guess: "))

    if guess != randNum:
        print("incorrect, try again")
        wrongGuesses += 1
        print(f"number of wrong guesses: {wrongGuesses}")

    else:
        print("correct")
        break

print("congrats, you win!")