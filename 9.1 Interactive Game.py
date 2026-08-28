import random

number = random.randint(1, 100)
attempts = 0

print("===== Number Guessing Game =====")
print("I have selected a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Higher! Try again.")

    elif guess > number:
        print("Lower! Try again.")

    else:
        print("Congratulations! You guessed the correct number.")
        print("Total attempts:", attempts)
        break