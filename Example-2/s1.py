# Number guessing game
# Solution 1: mistakes

guess = 1

while True:
    num = input("Please guess the number between (0-100): ")
    try:
        num = int(num)
    except ValueError:
        print("Invalid number, please guess again.")

    if num < 45:
        print("Your guess was low.")
    elif num > 45:
        print("Your guess was high.")
    else:
        break

    guess += 1


print(f"You guessed it in {guess} guesses.")
