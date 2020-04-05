# Number guessing game
# Solution 1: Better


class GuessNumber:
    def __init__(self, number, min=0, max=100):
        self.number = number
        self.min = min
        self.max = max
        self.guesses = 0

    def get_guesses(self):
        guess = input(f"Please enter a number ({self.min} - {self.max}): ")

        if self.valid_number(guess):
            return int(guess)
        else:
            print("Please enter a valid number.")
            return self.get_guesses()

    def valid_number(self, n):
        try:
            number = int(n)
        except ValueError:
            return False

        return self.min <= number <= self.max

    def play(self):
        while True:
            self.guesses += 1
            guess = self.get_guesses()

            if guess < self.number:
                print("Your guess was low.")
            elif guess > self.number:
                print("Your guess was high.")
            else:
                break
        print(f"You guessed it in {self.guesses} guesses.")


game = GuessNumber(50, 40, 60)
game.play()
