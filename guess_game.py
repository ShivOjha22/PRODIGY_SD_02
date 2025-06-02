import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    while True:
        number_to_guess = random.randint(1, 100)
        attempts = 0
        guessed = False

        print("\nI have generated a random number between 1 and 100.")
        print("Can you guess what it is?")

        while not guessed:
            try:
                user_guess = int(input("Enter your guess: "))
                attempts += 1

                if user_guess < number_to_guess:
                    print("Too low! Try again.")
                elif user_guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    guessed = True
                    print(f"Congratulations! You've guessed the number {number_to_guess} correctly.")
                    print(f"It took you {attempts} attempts to win the game.")
            except ValueError:
                print("Please enter a valid number.")

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing! Goodbye!")
            break

number_guessing_game()
