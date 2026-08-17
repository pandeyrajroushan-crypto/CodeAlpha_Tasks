# Hangman Game (Python)

## Overview

This is a simple command-line Hangman game developed in Python. The game randomly selects a word from a predefined list, and the player must guess the word one letter at a time before reaching the maximum number of incorrect guesses.

---

## Features

- Random word selection
- Command-line interface
- Input validation
- Displays guessed letters
- Tracks incorrect guesses
- Win and loss detection
- Option to play multiple rounds

---

## Technologies Used

- Python 3
- `random` module

---

## Project Structure

```text
Hangman/
├── hangman.py
└── README.md
```

---

## Requirements

- Python 3.x installed on your system

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/hangman-game.git
```

Move to the project directory:

```bash
cd hangman-game
```

---

## Running the Application

```bash
python hangman.py
```

or

```bash
python3 hangman.py
```

---

## How to Play

1. The game selects a random word.
2. The word is displayed as underscores.
3. Enter one letter at a time.
4. Correct guesses reveal letters in the word.
5. Incorrect guesses reduce the remaining attempts.
6. The game ends when the word is guessed or the maximum number of incorrect guesses is reached.

---

## Example

```text
========================================
WELCOME TO HANGMAN
========================================

Word: _ _ _ _ _ _

Guess a letter: a

Good guess!

Word: _ a _ _ a _
```

---

## Concepts Used

- Functions
- Lists
- Strings
- Loops
- Conditional Statements
- User Input
- Random Module
- Input Validation

---

## Customization

- Add more words to the `WORDS` list
- Change the maximum number of wrong guesses
- Update the Hangman ASCII art
- Add categories or difficulty levels

---

## Future Enhancements

- Difficulty levels
- Hint system
- Score tracking
- Word categories
- Colored terminal output
- GUI version using Tkinter or PyQt

---

## License

This project is intended for educational and learning purposes. You are free to use and modify it.

---

## Author

**Raj Raushan Pandey**

Computer Science Engineering Student
