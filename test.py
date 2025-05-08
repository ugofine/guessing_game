def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("Try to guess the number I'm thinking of.")
    print("You have 5 attempts!")

    secret_number = 42
    attempts_left = 5
    guessed_correctly = False  # Flag to track if user guessed the number

    while attempts_left > 0:
        try:
            guess = int(input(f"\nEnter your guess ({attempts_left} attempts left): "))
            attempts_left -= 1

            if guess < secret_number:
                print("📉 Too low!")
            elif guess > secret_number:
                print("📈 Too high!")
            else:
                print(f"🎉 Correct! The number was {secret_number}.")
                print(f"You got it in {5 - attempts_left} attempts.")
                guessed_correctly = True
                break
        except ValueError:
            attempts_left -= 1
            print("🚫 Invalid input! That counts as an attempt.")

    # Game over message if not guessed correctly
    if not guessed_correctly:
        print("\n❌ Game Over! You've used all your attempts.")
        print(f"The correct number was: {secret_number}")
