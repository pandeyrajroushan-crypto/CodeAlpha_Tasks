"""
Simple Hangman Game
Key concepts: random, while loop, if-else, strings, lists
"""

import random

WORDS = ["python", "hangman", "computer", "keyboard", "elephant"]
MAX_WRONG_GUESSES = 6

HANGMAN_STAGES = [
    """
       ------
       |    |
       |
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |    |
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    ---------
    """,
    """
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    ---------
    """
]


def choose_word():
    """Randomly select a word from the word list."""
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    """Show the word with guessed letters revealed and others as underscores."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    word = choose_word()
    guessed_letters = []
    wrong_guesses = 0

    print("=" * 40)
    print("  WELCOME TO HANGMAN")
    print("=" * 40)
    print(f"The word has {len(word)} letters. You have {MAX_WRONG_GUESSES} wrong guesses allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(HANGMAN_STAGES[wrong_guesses])
        print("Word: " + display_word(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")

        # Check for win condition
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word: " + word)
            break

        guess = input("\nGuess a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print(">> Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print(">> You already guessed that letter. Try again.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f">> Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f">> Sorry, '{guess}' is not in the word.\n")

        # Re-check win condition after guess
        if all(letter in guessed_letters for letter in word):
            print(HANGMAN_STAGES[wrong_guesses])
            print("Word: " + display_word(word, guessed_letters))
            print("\nCongratulations! You guessed the word: " + word)
            break
    else:
        # This runs only if the while loop exits WITHOUT a break (i.e., ran out of guesses)
        print(HANGMAN_STAGES[wrong_guesses])
        print(f"\nGame over! You ran out of guesses. The word was: {word}")


def main():
    play_again = "y"
    while play_again == "y":
        play_hangman()
        play_again = input("\nPlay again? (y/n): ").lower().strip()
    print("\nThanks for playing Hangman! Goodbye.")


if __name__ == "__main__":
    main()
